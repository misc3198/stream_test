import numpy as np
import pandas as pd
import streamlit as st
import datetime as dt

st.title("testaaaaa")
st.write("bbbbb")

now = dt.date.today()
year = int(now.strftime("%Y")) + 1

left_column, right_column = st.columns(2)

st.sidebar.write("siddebar_test")

button = left_column.button("ボタン")
if button:
    right_column.write("ボタン")

st.selectbox("year", list(range(2016, year)))
st.selectbox("month", list(range(1,13)))

if st.checkbox("option"):
    st.write("option")
    text = st.text_input("optionvalue")
    st.write(text)

df = pd.DataFrame([[1,2,3,4]])
st.dataframe(df, width = 1000, height = 500)