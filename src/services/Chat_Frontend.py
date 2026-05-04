import streamlit as st
#session state->dict -> not erase or reset and only reset the things when we erase this one
message_history=[]
for message in message_history:
    with st.chat_message(message['role']):
        st.text(message['content'])
user_input =st.chat_input("Type Here....")

if user_input:
    message_history.append({'role':"user",'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)
    message_history.append({'role':"user",'content':user_input})
    with st.chat_message("assistant"):
        st.text(user_input)