import streamlit as st
st.title("계산 결과 재사용")
@st.cache_data(ttl = 60)
def sum_squares(limit):
    return sum(n * n for n in range(limit + 1))

limit = st.number_input("끝 숫자", min_value = 1, max_value = 10000, value = 3)
with st.spinner("계산 중"):
    result = sum_squares(int(limit))
st.metric("제곱합", result)
if st.button("이 함수 캐시 지우기"):
    sum_squares.clear()
    st.success("캐시를 지웠습니다.")