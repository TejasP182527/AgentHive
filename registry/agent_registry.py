import sys
import os
sys.path.append('../')
from utils.logging import setup_logging
log = setup_logging()

class AgentRegistry:
    def __init__(self):
        self.registry = {}
    
    def register_agent(self, agent_id, agent_info):
        try:
            self. registry[agent_id] = agent_info
            log.info(f"Registered agent: {agent_id}")
            return True
        
        except Exception as e:
            log.error(f"Error registering agent '{agent_id}': {e}")
            return False

    def get_agent(self, agent_id):
        try:
            log.info(f"Retrieving agent: {agent_id}")
            agent_meta = self.registry.get(agent_id)
            if not agent_meta:
                log.error(f"Agent '{agent_id}' not found in registry.")
                return None

            return agent_meta['handler']()
        except Exception as e:
            log.error(f"Error retrieving agent '{agent_id}': {e}")
            return None

    def list_agents(self):
        try:
            log.info(f"Listing all registered agents:{list(self.registry.keys())}")
            return self.registry
        except Exception as e:
            log.error(f"Error listing agents: {e}")
            return {}