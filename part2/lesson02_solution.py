import streamlit as st

st.title("상품 소개")
st.markdown("편안함을 추구하는 젠틀리머 포켓가방")
st.sidebar.header("상품 목록")
st.sidebar.write("**젠틀리머 포켓가방**")
st.sidebar.write("젠틀리머 경추 베개")
left, right = st.columns(2)
with left:
    st.header("상품 설명")
    st.write("수납 공간이 10곳이나 되는 가방")
with right:
    st.header("가격 안내")
    st.write("39,700원")