from fastapi import FastAPI
from src.routes.llmroute import llmrouter
app = FastAPI()
#this is the tutorial for langgraph sequintial workflow
app.include_router(llmrouter)

@app.get("/echo")
def echo():
    return {"message": "Hello, World!"}