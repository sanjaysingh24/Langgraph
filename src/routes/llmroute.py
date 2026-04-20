from src.config.llm import agent
from fastapi import APIRouter
from src.schema.chatSchema import ChatResponse
router = APIRouter(prefix="/llm", tags=["llm"])

@router.post("/agent")
async def call_agent(data:ChatResponse):
    response = await agent(data.message)