import streamlit as st
st.title("단가 수량 계산기")
x = st.number_input("단가", min_value = 1, value = 1000)
y = st.number_input("수량", min_value = 1, value = 5)

st.metric("더하기:", f"{x + y}원")
st.metric("빼기:", f"{x - y}원")
st.metric("곱하기:", f"{x * y}원")
st.metric("나누기:", f"{x / y}원")
