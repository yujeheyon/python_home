import streamlit as st

st.set_page_config(page_title = "학습 안내", layout = "wide")
st.title("개발자 초급반")
st.markdown("**오늘 목표**: 입력과 결과를 구분합니다.")
st.sidebar.header("학습 안내")
st.sidebar.write("총 60시간")
left, right = st.columns(2)
with left:
    st.header("입력")
    st.write("왼쪽에서 조건을 고릅니다.")
with right:
    st.header("결과")
    st.write("오른쪽에서 결과를 확인합니다.")