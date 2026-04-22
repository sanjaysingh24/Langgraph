from langgraph.graph import StateGraph,START,END
from langchain_huggingface import ChatHuggingFace

from src.schema.chatSchema import LLMState
from typing import TypedDict
from src.config.llm import AgentConfig
agent_config = AgentConfig()
model = ChatHuggingFace(llm=agent_config.llm)

#define state
def llmqa(state:LLMState)->LLMState:
    question = state['question']
    #form a prompt 
    prompt = f"Answer the following question: {question}"
    #ask to the llm 
    answer = model.invoke(prompt).content

    #update answer in the state
    state['answer']  = answer
    return state
    
graph = StateGraph(LLMState)
def langgraphllm(message:str):
    #add node
    graph.add_node("llm_qa",llmqa)
    #add_edge
    graph.add_edge(START,"llm_qa")
    graph.add_edge("llm_qa",END)
    #compile graph
    workflow = graph.compile()
    #execute
    intialstate = {'question': message}
    final_state= workflow.invoke(intialstate)
    print(final_state)
    return final_state['answer']