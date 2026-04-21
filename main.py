from fastapi import FastAPI
from src.routes.llmroute import llmrouter
app = FastAPI()
#this is the tutorial for langgraph sequintial workflow
app.include_router(llmrouter)
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/echo")
def echo(message: str):
    return {"message": message}