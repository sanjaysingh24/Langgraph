from pydantic import BaseModel
from typing import TypedDict
class ChatRequest(BaseModel):
    message:str

class LLMState(TypedDict):
    question:str
    answer:str

class BlogState(TypedDict):
    title:str
    outline:str
    content:str

class ParallelState(TypedDict):
    text:str
    sentiment:str
    summary:str
    finalOutput:str

class ParallelRequest(BaseModel):
    text:str