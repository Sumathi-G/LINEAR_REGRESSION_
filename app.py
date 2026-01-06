import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My First Streamlit App", layout="centered")

st.title("🚀 Streamlit Demo App")
st.write("This is a simple Streamlit application")

# User input
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)

if st.button("Submit"):
    st.success(f"Hello {name}! You are {age} years old 🎉")

st.divider()

# Random data example
st.subheader("📊 Random Data Table")
data = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["Column A", "Column B", "Column C"]
)
st.dataframe(data)

st.divider()

# Chart
st.subheader("📈 Line Chart")
st.line_chart(data)