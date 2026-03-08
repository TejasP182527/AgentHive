import sys
import os
sys.path.append('../')
from registry.agent_registry import AgentRegistry
from agents.travel_agent.agent import TravelAgent
from agents.cooking_agent.agent import CookingAgent
from agents.finance_agent.agent import FinanceAgent
from agents.interview_coach.agent import InterviewCoach
from agents.research_assistant.agent import ResearchAssistant

agr = AgentRegistry()

#registering agents here
agr.register_agent(
    'TRAVEL_AGENT', {
        "name": "Travel Agent",
        "description": "Handles queries related to travel planning, bookings, and recommendations.",
        "handler": TravelAgent,
        "capabilities": [
            "trip planning",
            "travel itineraries",
            "destionation suggestions",
            "budget estimation"
        ],
        "examples":[
            "I am planning a trip to Austria. Give me a detailed itinerary",
            "Create in detailed trvel plan to explore the scenic beauty of Europe"
        ]
    }
)

#registering Cooking Agent
agr.register_agent(
    'COOKING_AGENT', {
        "name": "Cooking Assistant",
        "description": "Handles queries related to recipes, cooking techniques, and meal planning.",
        "handler": CookingAgent,
        "capabilities": [
            "recipe suggestions",
            "cooking techniques",
            "meal planning",
            "ingredient substitutions"
        ],
        "examples":[
            "I have chicken, tomatoes, and rice. What can I cook for dinner?",
            "Give me a recipe for a vegan chocolate cake."
        ]
    }
)

#registering Finance Agent
agr.register_agent(
    'FINANCE_AGENT', {
        "name": "Finance Agent",
        "description": "Handles queries related to personal finance, budgeting, and investment advice.",
        "handler": FinanceAgent,
        "capabilities": [
            "personal finance advice",
            "budgeting tips",
            "investment strategies",
            "financial planning"
        ],
        "examples":[
            "How can I save more money each month?",
            "What are some good investment options for a beginner?"
        ]
    }
)

#registering Interview Coach Agent
agr.register_agent(
    'INTERVIEW_COACH', {
        "name": "Interview Coach",
        "description": "Handles queries related to interview preparation, resume building, and career advice.",
        "handler": InterviewCoach,
        "capabilities": [
            "interview preparation",
            "resume building",
            "career advice",
            "job search strategies"
        ],
        "examples":[
            "How should I prepare for a software engineering interview?",
            "Can you help me improve my resume for a marketing position?"
        ]
    }
)

#registering Research Assistant Agent
agr.register_agent(
    'RESEARCH_ASSISTANT', {
        "name": "Research Assistant",
        "description": "Handles queries that require in-depth research, data analysis, and information synthesis across various topics.",
        "handler": ResearchAssistant,
        "capabilities": [
            "in-depth research",
            "data analysis",
            "information synthesis",
            "report generation"
        ],
        "examples":[
            "Can you provide a comprehensive overview of the current state of renewable energy technologies?",
            "I need a detailed report on the impact of social media on mental health."
        ]
    }
)