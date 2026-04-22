
from src.services.llmlanggraph import langgraphllm
from fastapi import APIRouter
from src.schema.chatSchema import ChatRequest
llmrouter = APIRouter(prefix="/llm", tags=["llm"])

@llmrouter.post("/llmgraph")
async def call_agent(data:ChatRequest):
    response = langgraphllm(data.message)
    return response