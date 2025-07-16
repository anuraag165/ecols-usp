import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Results Dashboard")

# Example data
data = {
    "Model": ["SVM", "Random Forest", "CNN", "tLSTM"],
    "Accuracy": [0.81, 0.85, 0.88, 0.92],
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("Model"))
