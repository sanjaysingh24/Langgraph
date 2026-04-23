from langchain_huggingface import ChatHuggingFace
from src.config.llm import AgentConfig
from langgraph.graph import StateGraph,START,END
from src.schema.chatSchema import BlogState
agent = AgentConfig()


model = ChatHuggingFace(llm=agent.llm)

graph = StateGraph(BlogState)


def create_outline(state:BlogState)->BlogState:
    #fetch the title
    title = state['title']
    #form a prompt
    
    #call llm 


    #generat a outline 


    #update the state and return
def generate_blog(message:str):
    graph.add_node("create_outline",create_outline)
    graph.add_node("create_blog",create_blog)