import streamlit as st

st.set_page_config(page_title= "첫 웹", layout= "centered")
st.title("나의 첫 Streamlit 웹")
st.write("파이썬으로 만든 웹 화면입니다.")
st.write("계산 결과: ", 8000 * 3)