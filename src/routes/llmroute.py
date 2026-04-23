
from src.services.llmlanggraph import langgraphllm
from fastapi import APIRouter
from src.schema.chatSchema import ChatRequest
from src.services.llmblog import generate_blog
llmrouter = APIRouter(prefix="/llm", tags=["llm"])

@llmrouter.post("/llmgraph")
async def call_agent(data:ChatRequest):
    response = langgraphllm(data.message)
    return response

@llmrouter.post("/bloggenerate")
async def generate(data:ChatRequest):
    response = generate_blog(data.message)
    return response