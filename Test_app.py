import streamlit as st
import seaborn as sns
st.header("Hello World")
st.text(" I am enjoying in learning the streamlit app")
st.header("This is a header")
pd=sns.load_dataset("iris")
st.write(pd[["species", "petal_length", "petal_width"]])
st.bar_chart(pd["sepal_length"])
st.line_chart(pd["sepal_width"])