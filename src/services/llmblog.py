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
   
    prompt = f"Create an outline for a blog post with the title: {title}"
    
    outline =  model.invoke(prompt).content
    state['outline'] = outline
    return state
  
def generate_blog(message:str):
    graph.add_node("create_outline",create_outline)
    graph.add_node("create_blog",create_blog)