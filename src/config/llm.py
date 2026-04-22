import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    max_new_tokens=1000,
)
parser = StrOutputParser()

model = ChatHuggingFace(llm=llm)

final_output = model | parser
def agent(message:str):
    response =  final_output.invoke(message)
    return response

