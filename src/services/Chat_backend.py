import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_huggingface import ChatHuggingFace
from src.config.llm import AgentConfig
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()

#initalize the chat model one
Textllm = AgentConfig()
llm_config = Textllm.llm
model = ChatHuggingFace(llm=llm_config)

#define the state then 
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

#initalize the graph
#initalize the checkpointer as well

checkpointer = InMemorySaver()
graph = StateGraph(ChatState)


