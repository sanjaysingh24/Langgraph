from langgraph.graph import StateGraph,START,END
from src.config.llm import AgentConfig
from langchain_huggingface import ChatHuggingFace
from src.schema.chatSchema import ParallelState

#initalize the llm agent
agent = AgentConfig()
model = ChatHuggingFace(llm=agent.llm)


#initalize the graph 
graph = StateGraph(ParallelState)

#define the business logic for the code

def sentiment_gen(state:ParallelState):
    text = state['text']
    prompt = f"Analyze the sentiment of the following text: {text}"
    sentiment = model.invoke(prompt).content
    
    return {'sentiment':sentiment}

def summary_gen(state:ParallelState):
    text = state['text']
    prompt = f"Generate a proper summary of the following text {text}"
    summary = model.invoke(prompt).content
    return {'summary':summary}

def final

def parrllel(message:str):
    #add a graph node 
    
    graph.add_node("sentiment_generate",sentiment_gen)
    graph.add_node("summary_generate",summary_gen)
    graph.add_node("final_output_generate",final_output_gen)

    #add edges

