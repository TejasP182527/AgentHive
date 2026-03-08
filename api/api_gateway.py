import sys
import os
sys.path.append('../')
import uuid
import asyncio
from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from core.orchestrator_agent import OrchestratorAgent
from memory.session_manager import store_interaction, get_history
from utils.logging import setup_logging
log = setup_logging()

app = FastAPI(title="AgentHive", description="API Gateway for routing user queries to specialized agents", version="1.0")

orchestrator = OrchestratorAgent()
executor = ThreadPoolExecutor(max_workers=2)

class HealthCheckResponse(BaseModel):
    success: str

class QueryRequest(BaseModel):
    user_id: str = Field(..., min_length=1, description="Unique identifier for the user")
    query: str = Field(..., min_length=1, max_length=1000, description="The user's query text")

class QueryResponse(BaseModel):
    response: str
    session_id: Optional[str] = None

@app.get("/", status_code=200)
async def health():
    log.info(f"Healthcheck endpoint called...")
    return HealthCheckResponse(success="AgentHive API is up and running...")

@app.post("/query", response_model=QueryResponse)
async def start_query(request: QueryRequest):
    '''
    Endpoint to receive user queries and route them to the appropriate agents through the Orchestrator Agent.
    '''
    try:
        session_id = f"{request.user_id}_{str(uuid.uuid4())}"
        log.info(f"Received query for session_id: {session_id}")
        response = orchestrator.handle_query(session_id, request.query)
        log.info(f"Response for session_id {session_id}: {response}")
        return QueryResponse(response=response, session_id=session_id)
        
    except ValueError as ve:
        log.error(f"Validation error for user_id: {request.user_id} - {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    
    except Exception as e:
        log.error(f"Error processing query for user_id: {request.user_id} - {e}")
        raise HTTPException(status_code=500, detail="Sorry, an error occurred while processing your query. Please try again later.")

@app.get("/history")
async def get_user_history(session_id: str):
    '''
    Endpoint to retrieve the interaction history for a given user session.
    '''
    try:
        log.info(f"Received history request for session_id: {session_id}")
        history = get_history(session_id)
        return {"history": history}
    except Exception as e:
        log.error(f"Error retrieving history for session_id: {session_id} - {e}")
        raise HTTPException(status_code=500, detail="Sorry, an error occurred while retrieving your history. Please try again later.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8855)