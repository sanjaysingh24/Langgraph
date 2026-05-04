import streamlit as st

with st.chat_message('user'):
    st.text('Hii bro')

with st.chat_message('assistant'):
    st.text("How can i help You")

with st.chat_message('user'):
    st.text("My name is Sanjay")


user_input =st.chat_input("Type Here....")

if user_input:
    with st.chat_message('user'):
        st.text(user_input)