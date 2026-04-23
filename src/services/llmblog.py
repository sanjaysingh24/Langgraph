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
def create_blog(state:BlogState)->BlogState:
    outline = state['outline']
    #form a prompt
    prompt = f"Write a blog post based on the following outline:{outline}"
    blog = model.invoke(prompt).content
    state['content'] = blog
    return state
def generate_blog(message:str):
    graph.add_node("create_outline",create_outline)
    graph.add_node("create_blog",create_blog)

    #add edges
    graph.add_edge(START,"create_outline")
    graph.add_edge("create_outline","create_blog")
    graph.add_edge("create_blog",END)

    #compile the graph
    workflow = graph.compile()

    #execute the graph
    initial_state ={'title':message}
    final_state = workflow.invoke(initial_state)
    print(final_state)