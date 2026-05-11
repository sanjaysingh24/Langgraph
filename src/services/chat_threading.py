import streamlit as st
from Chat_backend import chatbot
from langchain_core.messages import HumanMessage
#generate a random id
import uuid
#session state->dict -> not erase or reset and only reset the things when we erase this one

#create a utilty function to generate a random thread id
#everytime it generate a new thread id 
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id
thread_id =1

if 'message_history' not in st.session_state:
    st.session_state['message_history'] =[]
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
# side bar
st.sidebar.title("Langgraph Chat bot")
st.sidebar.button("New Chat")
st.sidebar.header("My Conversations")
st.sidebar.text(st.session_state['thread_id'])

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])
user_input =st.chat_input("Type Here....")

if user_input:
    st.session_state['message_history'].append({'role':"user",'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    config = {'configurable':{'thread_id':st.session_state['thread_id']}}
    with st.chat_message("assistant"):
       ai_message =  st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream({"messages":[HumanMessage(content=user_input)]},config=config,
                           stream_mode="messages")
        )
    st.session_state["message_history"].append({'role':"assistant",'content':ai_message})