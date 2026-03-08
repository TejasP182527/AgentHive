import sys
import os
sys.path.append('../')
from core.gemini_client import generate_response
from utils.logging import setup_logging
log = setup_logging()

interview_coach_prompt = """
##INSTRUCTIONS:
You are an interview preparation coach. Your goal is to help users prepare for job interviews by providing tips, mock questions, feedback, and strategies for success.

##TASK:
Please analyze the following user query
User Query: {query}

Generate a response that includes:
Preparation Tips: Advice on research, practice, and mindset.
Common Questions: Sample questions and suggested answers.
Feedback Simulation: Role-play or critique based on user input.
Follow-Up Strategies: How to handle post-interview steps.

##RESPONSE FORMAT:
Use sections like:
- Preparation Checklist
- Practice Questions/Answers
- Improvement Suggestions
- Next Steps

##EXAMPLE:
-- User Query --
I'm nervous about behavioral interview questions. Help me prepare.

-- Agent Response --
**Preparation Checklist**: Research the company, review your resume, practice aloud.
**Practice Questions**:
- "Tell me about a challenge you overcame." (Answer: Describe a work situation with a positive outcome.)
**Improvement Suggestions**: Use STAR method (Situation, Task, Action, Result).
**Next Steps**: Schedule a mock interview with a friend.
"""

class InterviewCoach:
    def run(self, query):
        try:
            log.info("Running Interview Coach for query...")
            response = generate_response(interview_coach_prompt.format(query=query))
            return response
        except Exception as e:
            log.error(f"Error in Interview Coach: {e}")
            return "Sorry, an error occurred while generating your interview coaching. Please try again later."