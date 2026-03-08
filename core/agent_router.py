import sys
import os
sys.path.append('../')
from core.gemini_client import generate_response
from registry.registered_agents import agr
import json
from utils.logging import setup_logging
log = setup_logging()

def route_agent(query):
    '''
    Understand user query and route it to the appropriate agent based on the content and context of the query.
    '''
    try:
        available_agents = agr.list_agents()
        agent_descriptions = ""
        for agent_name, agent_info in available_agents.items():
            agent_descriptions += f"""
            Agent ID: {agent_name}
            Description: {agent_info['description']}
            Capabilities: {', '.join(agent_info['capabilities'])}
            """
        log.info(f"Routing query....")
        
        routing_instructions = """
        INSTRUCTIONS:
        You are an intelligent agent router. Your task is to analyze user queries and determine which specialized agent is best suited to handle the query based on its content and context.
        AVAILABLE AGENTS:
        {agent_descriptions}

        TASK:
        Please analyze the following user query and determine which agent is best suited to handle it. Consider the content, context, and intent of the query in your analysis.
        User Query: {query}

        RESPONSE FORMAT:
        Your response should be a JSON object with the following structure:
        {{
            "agent": "Name of the selected agent from the list above OR 'None' if no suitable agent is found",
            "reasoning": "A clear explanation of why this agent is best suited to handle the query."
        }}

        NOTE:
        - If the query is ambiguous and could potentially fit multiple agents, choose the one that seems most relevant based on the primary intent of the query and provide a clear explanation for your choice.
        - If the query does not fit any of the agents, return "None" for the agent and provide an explanation.
        - Do NOT return response with ```json or any other markdown formatting, return only the JSON object as specified above.
        """

        result = generate_response(routing_instructions.format(query=query, agent_descriptions=agent_descriptions))
        log.info(f"Routing result: {result.strip().lower()}")
        return json.loads(result)
    
    except Exception as e:
        log.error(f"Error during agent routing: {e}")
        return {
            "agent": "None",
            "reasoning": "An error occurred during agent routing, but the system is allowing the query to pass without being handled by a specialized agent to avoid disruption of user experience."
        }