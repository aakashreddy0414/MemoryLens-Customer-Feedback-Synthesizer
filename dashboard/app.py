import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Feedback Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Feedback Synthesizer")

st.subheader("January vs March Feedback")

# Data
data = {
    "Month": ["January", "March"],
    "Positive Feedback": [7, 11],
    "Negative Feedback": [8, 4]
}

df = pd.DataFrame(data)

# Display table
st.dataframe(df, use_container_width=True)

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Feedback", 30)

with col2:
    st.metric("Positive Change", "+4")

with col3:
    st.metric("Negative Change", "-4")

# Chart
st.subheader("Feedback Comparison")

chart_data = df.set_index("Month")

st.bar_chart(
    chart_data[["Positive Feedback", "Negative Feedback"]]
)

st.subheader("AI-Style Insight")

st.info(
    "Customers discussed Battery most frequently. "
    "Positive feedback increased from January to March, "
    "while negative feedback decreased."
)