
from src.services.llmlanggraph import langgraphllm
from fastapi import APIRouter
from src.schema.chatSchema import ChatRequest,ParallelRequest
from src.services.llmblog import generate_blog
from src.services.parallel import parallel
llmrouter = APIRouter(prefix="/llm", tags=["llm"])

@llmrouter.post("/llmgraph")
async def call_agent(data:ChatRequest):
    response = langgraphllm(data.message)
    return response

@llmrouter.post("/bloggenerate")
async def generate(data:ChatRequest):
    response = generate_blog(data.message)
    return response

@llmrouter.post("/parallelworkflow")
async def parallel_workflow(data:ParallelRequest):
    response = parallel(data.text)
    return response