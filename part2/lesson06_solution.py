import streamlit as st
if "score" not in st.session_state:
    st.session_state.score = 0
if st.button("10 증가"):
    st.session_state.score += 10
if st.button("5 감소"):
    st.session_state.score = max(0, st.session_state.score - 5)
st.metric("점수: ", st.session_state.score)