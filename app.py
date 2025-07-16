import streamlit as st
from PIL import Image

st.set_page_config(page_title="ECOLS Showcase", page_icon="🧪", layout="wide")

# Logo + Title
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/ecols_logo.png", width=100)
with col2:
    st.title("ECOLS - USP AI Research Showcase")

st.markdown("""
Welcome to the official platform for **ECOLS** at **USP**, where we showcase research papers, AI-driven projects, and interactive model demos focused on social impact and mental health analysis.

Use the sidebar to explore:
- 📄 Research Papers  
- 🔬 Projects  
- 🧠 AI Demos  
- 📈 Results Dashboard  
""")