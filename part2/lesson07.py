import streamlit as st
st.title("주문 미리보기")
with st.form("order_form"):
    name = st.text_input("이름")
    raw = st.text_input("수량", value = "1")
    submited = st.form_submit_button("계산")
if submited:
    st.session_state.pop("result", None)
    try:
        quantity = int(raw)
        if not name.strip() or not 1 <= quantity <= 100:
            raise ValueError("이름과 1~100의 수량을 입력하세요.")
        st.session_state.result = quantity * 8000
    except ValueError:
        st.error("이름과 1~100의 정수 수량을 확인하세요.")
if "result" in st.session_state:
    st.metric("총액", f"{st.session_state.result:,}원")