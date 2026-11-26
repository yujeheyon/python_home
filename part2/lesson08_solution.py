import streamlit as st

if "messages" not in st.session_state:
    st.session_state.messages = []

question = st.chat_input("질문")
if question and question.strip():
    st.session_state.messages += [
        {"role": "user", "content": question},
        {"role": "assistant", "content": f"길이: {len(question)}"}
    ]
    st.session_state.messages = st.session_state.messages[-10:]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])