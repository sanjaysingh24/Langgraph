from src.config.llm import agent
from fastapi import APIRouter
from src.schema.chatSchema import ChatRequest
llmrouter = APIRouter(prefix="/llm", tags=["llm"])

@llmrouter.post("/agent")
async def call_agent(data:ChatRequest):
    response = agent(data.message)
    return response