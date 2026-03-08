'''
Session Manager for storing user interactions in Redis.
'''
import sys
import os
sys.path.append('../')
import os
import uuid
from memory.redis_client import redis_client
from utils.logging import setup_logging
log = setup_logging()

def store_interaction(session_id, query, response):
    '''
    Stores a user query and the corresponding response in Redis.
    '''
    try:
        log.info(f"Storing interaction for session: {session_id}")
        date_time = str(uuid.uuid1())
        redis_client.rpush(
            session_id,
            str({
                'query': query, 
                'response': response
            }),
            str(date_time)
        )
        return True
    
    except Exception as e:
        log.error(f"Error storing interaction for session_id: {session_id} - {e}")
        return False

def get_history(session_id):
    '''
    Retrieves the interaction history for a given user ID.
    '''
    try:
        log.info(f"Retrieving history for session_id: {session_id}")
        keys = redis_client.keys(session_id)
        history = []
        for key in keys:
            interactions = redis_client.lrange(key, 0, -1)
            history.extend(interactions)
        return history

    except Exception as e:
        log.error(f"Error retrieving history for session_id: {session_id} - {e}")
        return []