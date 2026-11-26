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
df["avg"] = df["score"].sum() / 3
st.metric("평균: ", f"{df["avg"]}점")