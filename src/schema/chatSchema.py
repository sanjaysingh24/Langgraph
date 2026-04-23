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