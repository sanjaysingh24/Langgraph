import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id=os.getenv("HF_LLM_REPO_ID"),
    task=os.getenv("HF_LLM_TASK"),
    max_new_tokens=int(os.getenv("HF_LLM_MAX_NEW_TOKENS", 2048))
)
model = ChatHuggingFace(llm=llm)

async def agent(message:str):
    response =  model.invoke(message)
    print(response)

