import streamlit as st
st.title("1부터 n까지의 합계")
@st.cache_data(ttl = 30)
def total(n):
    return sum(range(1, n + 1))
n = st.number_input("n", min_value = 1, value = 10)
with st.spinner("계산 중"):
    result = total(int(n))
st.write(result)