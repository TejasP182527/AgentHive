import sys
import os
sys.path.append('../')
from utils.input_guardrails import guardrail_check
from core.agent_router import route_agent
from memory.session_manager import store_interaction
from registry.registered_agents import agr
from utils.logging import setup_logging
log = setup_logging()

class OrchestratorAgent:
    '''
    The Orchestrator Agent is responsible for managing the overall flow of user interactions. It performs the following tasks:
    1. Receives user queries and checks them against guardrails to ensure they are safe and appropriate.
    2. Routes the queries to the appropriate specialized agents based on their content and context.
    3. Stores the interactions in a session manager for future reference and analysis.
    '''
    
    def handle_query(self, session_id, query):
        try:
            log.info(f"Handling query for user_id: {session_id}")
            guardrail_result = guardrail_check(query)
            log.info(f"Guardrail check result for session_id {session_id}: {guardrail_result}")
            if guardrail_result['result'] == 'FAIL':
                response = f"Your query violates the following guardrails: {', '.join(guardrail_result['violated_guardrails'])}. Explanation: {guardrail_result['explanation']}"
                return response
            
            agent_id = route_agent(query)
            if agent_id['agent'] == 'None':
                response = f"No suitable agent found for your query. Reasoning: {agent_id['reasoning']}"
                store_interaction(session_id, query, response)
                return response
            
            agent = agr.get_agent(agent_id['agent'])
            if not agent:
                response = f"Selected agent '{agent_id['agent']}' is not available. Reasoning: {agent_id['reasoning']}"
                store_interaction(session_id, query, response)
                return response

            return agent.run(query)
        
        except Exception as e:
            log.error(f"Error in handle query for session_id: {session_id} - {e}")
            response = "Sorry, an error occurred while processing your query. Please try again later."
            store_interaction(session_id, query, response)
            return response