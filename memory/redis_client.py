'''
Redis client initialization and configuration.
'''
import sys
import os
sys.path.append('../')
import redis
from config.conf_settings import REDIS_HOST, REDIS_PORT
from utils.logging import setup_logging
log = setup_logging()

log.info(f"Initializing Redis client with host: {REDIS_HOST} and port: {REDIS_PORT}")
redis_client = redis.Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    decode_responses=True
)
log.info("Redis client initialized successfully")