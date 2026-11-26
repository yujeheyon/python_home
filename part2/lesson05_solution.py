import streamlit as st
from common import parse_sales

st.write("필수 열: product, quantity, price")
uploaded = st.file_uploader("CSV 파일", type= ["csv"])
if uploaded is None:
    st.info("csv 파일을 올려주세요.")
else:
    try:
        st.dataframe(parse_sales(uploaded.getvalue()))
    except ValueError as exc:
        st.error(str(exc))