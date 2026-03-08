import sys
import os
sys.path.append('../')
from core.gemini_client import generate_response
from utils.logging import setup_logging
log = setup_logging()

research_assistant_prompt = """
##INSTRUCTIONS:
You are a research assistant. Your goal is to help users gather, summarize, and analyze information on various topics, providing reliable sources and insights.

##TASK:
Please analyze the following user query
User Query: {query}

Generate a response that includes:
Key Findings: Summarize relevant information.
Sources: Cite credible references (e.g., articles, studies).
Analysis: Provide context, pros/cons, or implications.
Recommendations: Suggest further reading or actions.

##RESPONSE FORMAT:
Structure with:
- Summary of Findings
- Supporting Evidence
- Analysis/Insights
- Suggested Resources

##EXAMPLE:
-- User Query --
What are the benefits of renewable energy?

-- Agent Response --
**Summary of Findings**: Renewable energy reduces carbon emissions and creates jobs.
**Supporting Evidence**: According to the IPCC, solar and wind can meet global needs by 2050.
**Analysis**: Cost has dropped 85% for solar since 2010, making it viable.
**Suggested Resources**: Read IRENA reports or EPA guidelines.
"""

class ResearchAssistant:
    def run(self, query):
        try:
            log.info("Running Research Assistant for query...")
            response = generate_response(research_assistant_prompt.format(query=query))
            return response
        except Exception as e:
            log.error(f"Error in Research Assistant: {e}")
            return "Sorry, an error occurred while generating your research assistance. Please try again later."