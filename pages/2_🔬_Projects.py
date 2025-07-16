import streamlit as st

st.title("🔬 ECOLS Projects")

projects = [
    {"name": "Social Media Depression Detection", "desc": "Detecting depressive content using hybrid deep learning."},
    {"name": "Multilingual Sentiment Analysis", "desc": "Real-time sentiment scoring across English, Hindi, Fijian."},
    {"name": "Voice-based AI Screening", "desc": "Using call center voice recordings to detect emotional distress."},
]

for p in projects:
    st.subheader(p["name"])
    st.markdown(p["desc"])
    st.markdown("---")
