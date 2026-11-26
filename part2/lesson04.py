import pandas as pd
import streamlit as st
st.title("상품별 매출")
rows= [
    {"product": "book", "quantity": 2, "price": 12000},
    {"product": "pen", "quantity": 5, "price": 1500}
]

df = pd.DataFrame(rows)
# revenue 라는 열을 추가 후 quantity의 값과 price의 값을 곱함
df["revenue"] = df["quantity"] * df["price"]
# 인덱스 번호를 빼고 보여주기 hide_index = True / False
st.dataframe(df, hide_index = True)
# bar_chart : 막대그래프로 시각화하는 코드
# df.set_index("") : 특정 열을 인덱스로 선택
# df.set_index("")[""] : 그래프로 나타낼 데이터 선택
st.bar_chart(df.set_index ("product")["revenue"])
st.metric("총매출", f"{int(df['revenue'].sum()):,}원")