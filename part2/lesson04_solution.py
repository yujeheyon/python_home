import pandas as pd
import streamlit as st

rows = [
    {"subject": "국어", "score": 80},
    {"subject": "수학", "score": 90},
    {"subject": "영어", "score": 100}
]

df = pd.DataFrame(rows)
st.dataframe(df, hide_index = True)
st.bar_chart(df.set_index("subject")["score"])

# 평균 계산
avg = df["score"].mean()
st.metric("평균: ", f"{avg:.1f}점")