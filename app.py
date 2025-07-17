import streamlit as st
from PIL import Image

st.set_page_config(page_title="ECOLS Showcase", page_icon="🧪", layout="wide")

# Custom CSS for styling
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
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        margin-bottom: 20px;
        background-color: #FFFFFF;
    }
    .social-icon {
        font-size: 24px;
        margin-right: 10px;
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

# Header Section with Logo
col1, col2 = st.columns([1, 5])
with col1:
    st.image("images/ecols_logo.png", width=120)
with col2:
    st.markdown("<h1 class='header'>ECOLS Research Group</h1>", unsafe_allow_html=True)
    st.markdown("""
    <h3 style='color: #6B6B6B;'>AI for Social Impact & Mental Health Analysis</h3>
    <p>The University of the South Pacific (USP) Research Initiative</p>
    """, unsafe_allow_html=True)

# Main Content
st.markdown("""
## 🌟 About ECOLS
The **ECOLS** (Evolutionary Computation & Learning Systems Research Group) research group at USP focuses on developing AI-driven solutions 
for mental health analysis, social impact assessment, and human-computer interaction. Our interdisciplinary approach 
combines machine learning, natural language processing, and psychological insights to create meaningful tools for society.
""")

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📄 Research", "🔬 Projects", "🧠 AI Demos", "📊 Dashboard"])

with tab1:
    st.header("Research Publications")
    st.markdown("""
    - **Mental Health Analysis through Social Media** (IEEE Access 2023)
    - **AI-powered Depression Detection** (Nature Scientific Reports 2024)
    - **Ethical AI for Social Good** (ACM Conference 2023)
    """)
    st.button("View All Publications →")

with tab2:
    st.header("Featured Projects")
    st.markdown("""
    <div class='project-card'>
        <h4>MindScope: Mental Health Monitoring Platform</h4>
        <p>Real-time analysis of textual and vocal cues for early mental health risk detection</p>
    </div>
    <div class='project-card'>
        <h4>SocialSentinel: Hate Speech Detection</h4>
        <p>Multilingual NLP system for identifying harmful content in social media</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Visit Project Repository", "https://github.com/ECOLS-research-group")

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
    st.markdown("""
    Coming soon! Our interactive dashboard will visualize research metrics, model performance, and impact statistics.
    """)

# Researchers Section
st.markdown("""
## 👨‍🔬 Research Team
Meet our dedicated team of researchers and developers:
""")

# Researcher Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='researcher-card'>
        <h3>Dr. Anuraganand Sharma</h3>
        <p>Principal Investigator<br>AI for Mental Health</p>
        <div>
            <a href="[Google Scholar Link]" class='social-icon'>📚</a>
            <a href="[ResearchGate Link]" class='social-icon'>🔬</a>
            <a href="[IEEE Xplore Link]" class='social-icon'>⚡</a>
            <a href="[ORCID Link]" class='social-icon'>🆔</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='researcher-card'>
        <h3>Anuraag Raj</h3>
        <p>Research Scientist<br>NLP & ML Engineering</p>
        <div>
            <a href="[Google Scholar Link]" class='social-icon'>📚</a>
            <a href="[ResearchGate Link]" class='social-icon'>🔬</a>
            <a href="[IEEE Xplore Link]" class='social-icon'>⚡</a>
            <a href="[Github Link]" class='social-icon'>💻</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='researcher-card'>
        <h3>Deshant Singh</h3>
        <p>Research Associate<br>Data Science & Analytics</p>
        <div>
            <a href="[Google Scholar Link]" class='social-icon'>📚</a>
            <a href="[ResearchGate Link]" class='social-icon'>🔬</a>
            <a href="[ORCID Link]" class='social-icon'>🆔</a>
            <a href="[Github Link]" class='social-icon'>💻</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p>🔗 <a href="https://github.com/ECOLS-research-group" target="_blank">ECOLS GitHub Repository</a></p>
    <p>📧 Contact us at: ecols-research@usp.br</p>
    <p>© 2025 ECOLS Research Group | The University of the South Pacific (USP)</p>
</div>
""", unsafe_allow_html=True)