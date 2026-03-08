# AgentHive 🐝

AgentHive is a beginner-friendly multi-agent AI system designed to help users with various tasks through specialized AI agents. Whether you need help with cooking recipes, travel planning, financial advice, interview coaching, or research assistance, AgentHive has you covered!

## Features

- **Multi-Agent System**: Specialized agents for different domains (Cooking, Travel, Finance, Interview Coaching, Research)
- **Intelligent Routing**: Automatically routes your queries to the most appropriate agent
- **Safety First**: Built-in guardrails to ensure safe and appropriate interactions
- **Session Memory**: Remembers your conversation history using Redis
- **Web Interface**: Easy-to-use web UI built with Dash
- **API Gateway**: RESTful API for programmatic access
- **Powered by Gemini**: Uses Google's Gemini AI for intelligent responses

## Architecture

AgentHive consists of several key components:

- **API Gateway** (`api/api_gateway.py`): FastAPI-based entry point for handling user queries
- **Orchestrator Agent** (`core/orchestrator_agent.py`): Manages query flow, guardrails, and routing
- **Agent Router** (`core/agent_router.py`): Intelligently routes queries to specialized agents
- **Specialized Agents** (`agents/`): Domain-specific AI assistants
- **Memory System** (`memory/`): Redis-based session storage
- **Registry** (`registry/`): Manages available agents
- **UI** (`ui/app.py`): Web interface for user interactions
- **Utils** (`utils/`): Logging, guardrails, and helper functions

## Quick Start

### Prerequisites

- Python 3.11 or higher
- A Google Gemini API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))
- Redis server (for session memory)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/agenthive.git
   cd agenthive
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv agentenv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     agentenv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install fastapi pydantic redis google-generativeai python-dotenv dash requests
   ```

5. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   REDIS_HOST=localhost
   REDIS_PORT=6379
   ```

### Running AgentHive

1. **Start Redis server:**
   Make sure Redis is running on your system. If you don't have it installed, download from [redis.io](https://redis.io/download).

2. **Start the API Gateway:**
   ```bash
   python api/api_gateway.py
   ```
   The API will be available at `http://localhost:8855`

3. **Start the Web UI (in a new terminal):**
   ```bash
   python ui/app.py
   ```
   Open your browser and go to `http://localhost:8050`

## Usage

### Web Interface

1. Open the web UI in your browser
2. Enter your user ID (any unique identifier)
3. Type your query in the text area
4. Click "Submit Query"
5. View the agent's response

## Available Agents

- **Cooking Agent**: Recipes, meal planning, cooking techniques
- **Travel Agent**: Trip planning, itineraries, destination recommendations
- **Finance Agent**: Financial advice, budgeting, investment tips
- **Interview Coach**: Interview preparation, practice questions
- **Research Assistant**: General research and information gathering

## Configuration

- **API Settings**: Modify `config/conf_settings.py` for API endpoints and Redis config
- **Agent Prompts**: Customize agent behavior in `agents/*/agent.py`
- **Guardrails**: Adjust safety rules in `utils/input_guardrails.py`

## License
This project is created for learning purpose.

## Acknowledgments

- Powered by [Google Gemini](https://ai.google.dev/)
- Built with [FastAPI](https://fastapi.tiangolo.com/)
- UI with [Dash](https://dash.plotly.com/)
- Memory storage with [Redis](https://redis.io/)

Happy coding!