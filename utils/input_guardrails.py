import sys
import os
import json
sys.path.append('../')
from core.gemini_client import generate_response
from utils.logging import setup_logging
log = setup_logging()

def guardrail_check(query):
    '''
    Input:
    - query: The user query to be checked against guardrails.
    
    Output:
    - A dictionary containing the guardrail check result and any relevant messages.
    '''
    try:
        log.info(f"Starting guardrail check for query...")
        guardrails_instructions = """
        INSTRUCTIONS:
        You are a content moderation system. Your task is to analyze user queries and determine if they violate any of the following guardrails:

        CONSTRAINTS:        
        Hate Speech: Any content that promotes violence or hatred against individuals or groups based on attributes such as race, ethinicity, religion, gender, sexual orientation, disability, or any other characteristic.
        Harassment: Any content that targets individuals with the intent to harass, threaten, or bully.
        Misinformation: Any content that spreads false or misleading information, especially related to health, safety, or significant events.
        Explicit Content: Any content that contains sexually explicit material or graphic violence.
        Illegal Activities: Any content that promotes or facilitates illegal activities, such as drug use, human trafficking, or, violence.
        Self-Harm: Any content that promotes or encourages self-harm.
        Privacy Violations: Any content that shares personal information without consent.
        Data Exfilitration: Any content that attempts to extract sensitive information from the system or other users.
        Impersonation: Any content that attempts to impersonate another individual or entity
        Spam: Any content that is repetitive, irrelevant, or promotional in nature.

        TASK:
        Please analyze the following user query and determine if it violates any of the above guardrails. Provide a clear explanation for your decision.
        User Query: {query}

        RESPONSE FORMAT:
        Your response should return only one JSON object with the following structure:
        {{
            "result": "PASS" or "FAIL",
            "violated_guardrails": [list of violated guardrails, if any],
            "explanation": "A clear explanation of why the query passed or failed the guardrail check."
        }}

        NOTE:
        - Be thorough in your analysis and provide a clear explanation for your decision.
        - If the query violates multiple guardrails, list all that apply.
        - If the query is about handling personal finance, ignore it completely and return PASS, this should not be flagged as misinformation.
        - Do NOT return response with ```json or any other markdown formatting, return only the JSON object as specified above.
        """

        result = generate_response(guardrails_instructions.format(query=query))
        return json.loads(result)

    except Exception as e:
        log.error(f"Error during guardrail check: {e}")
        return {
            "result": "PASS",
            "violated_guardrails": [],
            "explanation": "An error occurred during guardrail check, but the query is being allowed to pass to avoid disruption of user experience."
        }