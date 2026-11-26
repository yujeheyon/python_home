import streamlit as st
st.title("신청 미리보기")
with st.form("email_form"):
    email = st.text_input("이메일")
    count = st.text_input("인원", value = "1")
    submit = st.form_submit_button("신청")
if submit:
    pcount = int(count)
    if "@" not in email:
        st.error("이메일 형식을 확인하세요.")
    elif not 1 <= pcount <= 10:
        st.error("1~10의 인원을 확인하세요.")
    else:
        st.write(f"이메일: {email}")
        st.write(f"인원: {pcount}")