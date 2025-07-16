import streamlit as st
import joblib

st.title("🧠 Depression Detection Demo")

text = st.text_area("Enter a sample Reddit or tweet post:")

if st.button("Predict"):
    model = joblib.load("data/depression_model.pkl")
    pred = model.predict([text])[0]
    st.success(f"Predicted label: **{pred}**")
