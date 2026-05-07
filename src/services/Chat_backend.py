import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()

#initalize the chat model one
llm = HuggingFaceEndpoint( 
    repo_id="Qwen/Qwen2.5-7B-Instruct",
            task="text-generation",
            max_new_tokens=2048)

model = ChatHuggingFace(llm=llm)

#define the state then 
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

#initalize the graph
#initalize the checkpointer as well

checkpointer = MemorySaver()
graph = StateGraph(ChatState)


#add nodes 
def chat_node(state:ChatState):
    message = state['messages']
    response = model.invoke(message)
    return{'messages':[response]}

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

chatbot = graph.compile(checkpointer=checkpointer)
