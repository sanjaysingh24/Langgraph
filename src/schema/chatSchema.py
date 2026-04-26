from pydantic import BaseModel,Field
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

class EvalutionSchema(BaseModel):
    feedback: str = Field(description ="Detailed feedback for the essay")
    score:int = Field(description = "Score out of 10",ge=0,le=10)