'''
This module provides a client for interacting with the Gemini API to generate responses based on prompts.
'''
import sys
import os
sys.path.append('../')
import google.generativeai as googai
from config.conf_settings import GEMINI_API_KEY
from utils.logging import setup_logging
log = setup_logging()

googai.configure(api_key=GEMINI_API_KEY)

model = googai.GenerativeModel('gemini-2.5-flash-lite')

def generate_response(prompt):
    '''
    Generates a response from the Gemini model based on the given prompt.
    '''
    try:
        log.info(f"Generating response....")
        response = model.generate_content(prompt)
        log.info(f"Response generated successfully: {response.text}")
        return response.text

    except Exception as e:
        log.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response at this time."