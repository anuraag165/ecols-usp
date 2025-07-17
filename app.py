import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="ECOLS Showcase", page_icon="🧪", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
    .header {
        color: #2E86AB;
        border-bottom: 2px solid #F18F01;
        padding-bottom: 10px;
    }
    .researcher-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        background-color: #FFFFFF;
    }
    .profile-name {
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 1.2em;
    }
    .profile-role {
        color: #6B6B6B;
        margin-bottom: 10px;
    }
    .social-icon {
        font-size: 20px;
        margin-right: 8px;
        color: #2E86AB;
    }
    .project-card {
        padding: 15px;
        border-left: 5px solid #F18F01;
        background-color: #F5F5F5;
        margin-bottom: 15px;
        border-radius: 0 8px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/ecols_logo.png", width=100)
with col2:
    st.markdown("<h1 class='header'>ECOLS Research Group</h1>", unsafe_allow_html=True)
    st.markdown("""
        <h3 style='color: #6B6B6B;'>Artificial Intelligence Research Initiative</h3>
        <p>Led by Dr. Anuraganand Sharma, University of the South Pacific (USP)</p>
    """, unsafe_allow_html=True)

# --- About Section ---
st.markdown("""
## 🌟 About ECOLS
The **Evolutionary Computation & Learning Systems (ECOLS)** group at USP drives cutting‑edge AI research 
across domains including natural language processing, computer vision, optimization, and ethical AI. 
Our interdisciplinary team develops novel models, algorithms, and applications to advance both theory 
and real‑world impact.
""")

# --- Navigation Tabs ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Research", 
    "🔬 Projects", 
    "🧠 AI Demos", 
    "📊 Dashboard"
])

with tab1:
    st.header("Research Publications")
    st.markdown("""
    - **Adaptive Evolutionary Algorithms for Real‑Time Control** (CEC 2024)  
    - **Transformer‑Based NLP for Social Media Analysis** (IEEE Access 2023)  
    - **Ethical Frameworks in Autonomous Systems** (ACM FAccT 2024)  
    """)
    st.button("View All Publications →")

with tab2:
    st.header("Featured Projects")
    st.markdown("""
    <div class='project-card'>
        <h4>MindScope: Mental Health Monitoring Platform</h4>
        <p>Real‑time analysis of textual and vocal cues for early mental health risk detection.</p>
    </div>
    <div class='project-card'>
        <h4>SocialSentinel: Hate Speech Detection</h4>
        <p>Multilingual NLP system for identifying harmful content in social media.</p>
    </div>
    <div class='project-card'>
        <h4>OptiPath: Logistics Optimization Engine</h4>
        <p>Evolutionary algorithms to improve supply chain routing efficiency.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("[Visit Project Repository →](https://github.com/ECOLS-research-group)")

with tab3:
    st.header("Interactive Demos")
    st.markdown("""
    - 🗣️ Speech Emotion Recognition  
    - 📝 Mental Health Text Analysis  
    - 🌐 Multilingual Sentiment Analysis  
    """)
    st.button("Try Our Demos →")

with tab4:
    st.header("Research Dashboard")
    st.markdown("Coming soon! Our interactive dashboard will visualize research metrics, model performance, and impact statistics.")

# --- Research Team ---
st.markdown("## 👨‍🔬 Research Team\nMeet our dedicated AI researchers and developers:")

cols = st.columns(3)
profiles = [
    {
        "name": "Dr. Anuraganand Sharma",
        "role": "Principal Investigator<br>AI & Evolutionary Computation",
        "interests": "Evolutionary algorithms, Ethical AI, Autonomous systems",
        "links": {
            "Google Scholar": "#",
            "ResearchGate": "#",
            "ORCID": "#",
            "IEEE Xplore": "#"
        }
    },
    {
        "name": "Anuraag Raj",
        "role": "Research Scientist<br>NLP & ML Engineering",
        "interests": "Transformer models, Depression detection, Social media analysis",
        "links": {
            "Google Scholar": "#",
            "ResearchGate": "#",
            "GitHub": "#",
            "LinkedIn": "#"
        }
    },
    {
        "name": "Deshant Singh",
        "role": "Research Associate<br>Data Science & Analytics",
        "interests": "Sentiment analysis, Time‑series forecasting, Visualization",
        "links": {
            "Google Scholar": "#",
            "ResearchGate": "#",
            "ORCID": "#",
            "GitHub": "#"
        }
    },
]

for col, profile in zip(cols, profiles):
    links_html = " ".join(
        f"<a href='{url}' class='social-icon' title='{name}'>{icon}</a>"
        for (name, url), icon in zip(profile["links"].items(), ["📚","🔬","🆔","💻"])
    )
    col.markdown(f"""
    <div class='researcher-card'>
        <div class='profile-name'>{profile["name"]}</div>
        <div class='profile-role'>{profile["role"]}</div>
        <p><strong>Interests:</strong> {profile["interests"]}</p>
        <div>{links_html}</div>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6B6B6B;'>
    <p>🔗 <a href="https://github.com/ECOLS-research-group" target="_blank">ECOLS GitHub Repository</a></p>
    <p>📧 Contact us at: ecols-research@usp.br</p>
    <p>© 2025 ECOLS Research Group | The University of the South Pacific (USP)</p>
</div>
""", unsafe_allow_html=True)
