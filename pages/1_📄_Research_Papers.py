import streamlit as st
from PIL import Image  # if you need it later

# Configure page
st.set_page_config(page_title="ECOLS Research Papers", page_icon="📄", layout="wide")

# -- Custom CSS for styling --
st.markdown(
    """
    <style>
        .paper-card {
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 12px 0 rgba(0,0,0,0.1);
            margin-bottom: 30px;
            background-color: #FFFFFF;
            border-left: 5px solid #4B8BBE;
            transition: transform 0.2s;
        }
        .paper-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px 0 rgba(0,0,0,0.15);
        }
        .paper-title {
            color: #2E86AB;
            margin-bottom: 10px !important;
        }
        .paper-authors {
            color: #6B6B6B;
            font-style: italic;
            margin-bottom: 8px !important;
        }
        .paper-meta {
            display: flex;
            gap: 15px;
            margin-bottom: 15px;
        }
        .paper-meta-item {
            display: flex;
            align-items: center;
            gap: 5px;
            color: #5F5F5F;
        }
        .paper-abstract {
            background-color: #F8F9FA;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        .tag {
            display: inline-block;
            background-color: #E3F2FD;
            color: #1976D2;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-right: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -- Header --
st.title("📄 ECOLS Research Publications")
st.markdown("Explore our latest research in AI for mental health and social media analysis")

# -- Paper 1 (updated) --
paper1_html = """
<div class="paper-card">
    <h2 class="paper-title">Depression Detection Using BERT on Social Media Platforms</h2>
    <p class="paper-authors">Anuraag Raj, Zain Ali, Shonal Chaudhary, Kavitesh Kumar Bali, Anuraganand Sharma</p>
    <div class="paper-meta">
        <span class="paper-meta-item">📅 Aug 2024</span>
        <span class="paper-meta-item">🏷️ <span class="tag">BERT</span> <span class="tag">Transformer</span> <span class="tag">Depression Detection</span></span>
        <span class="paper-meta-item">📊 IEEE IICAIET 2024</span>
    </div>
    <div class="paper-abstract">
        <strong>Abstract:</strong> Depression detection from social media has attracted significant attention due to its potential to offer early intervention and support to individuals facing mental health issues. In this study, we present a comprehensive evaluation of deep learning techniques for depression detection, with a specific focus on leveraging BERT, a powerful NLP Transformer model. Our exploration encompasses tailored preprocessing for social media text, diverse feature extraction methods, and optimized BERT-based model architectures. Through rigorous experimentation, we compare different strategies on accuracy, efficiency, and scalability, and analyze performance on both labeled and unlabeled data.
    </div>
    <a href="https://www.researchgate.net/profile/Anuraag-Raj/publication/385414089_Depression_Detection_Using_BERT_on_Social_Media_Platforms/links/6834014e026fee1034fbd774/Depression-Detection-Using-BERT-on-Social-Media-Platforms.pdf" target="_blank">
        <button style="background-color: #4B8BBE; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">
            📄 Read Full Paper
        </button>
    </a>
</div>
"""
st.markdown(paper1_html, unsafe_allow_html=True)

# -- Paper 2 (updated) --
paper2_html = """
<div class="paper-card">
    <h2 class="paper-title">Uncovering Depression with LSTM and NLP Transformers in Social Media Posts</h2>
    <p class="paper-authors">Anuraag Raj, Zain Ali, Shonal Chaudhry, Anuraganand Sharma</p>
    <div class="paper-meta">
        <span class="paper-meta-item">📅 2025</span>
        <span class="paper-meta-item">🏷️ <span class="tag">LSTM</span> <span class="tag">Transformers</span> <span class="tag">Depression Detection</span></span>
        <span class="paper-meta-item">📊 ResearchGate</span>
    </div>
    <div class="paper-abstract">
        <strong>Abstract:</strong> Depression detection from social media has garnered significant attention due to its potential to provide early intervention and support for individuals experiencing mental health challenges. In this study, we present a comprehensive comparative evaluation of the two most prominent state-of-the-art deep learning techniques for depression detection: Long Short-Term Memory (LSTM) networks and NLP Transformers, leveraging social media data to discern patterns indicative of depressive symptoms.
    </div>
    <a href="https://www.researchgate.net/profile/Anuraag-Raj/publication/392903166_Uncovering_Depression_with_LSTM_and_NLP_Transformers_in_Social_Media_Posts/links/68588ff207d6d53e82edb964/Uncovering-Depression-with-LSTM-and-NLP-Transformers-in-Social-Media-Posts.pdf" target="_blank">
        <button style="background-color: #4B8BBE; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">
            📄 Read Full Paper
        </button>
    </a>
</div>
"""
st.markdown(paper2_html, unsafe_allow_html=True)

# -- Sidebar filters --
with st.sidebar:
    st.header("🔍 Filter Publications")
    st.markdown("### By Year")
    years = ["All", "2023", "2020", "2019"]
    selected_year = st.selectbox("Select publication year", years)

    st.markdown("### By Topic")
    topics = ["All", "NLP", "Mental Health", "BERT", "Sentiment Analysis", "AI"]
    selected_topic = st.multiselect("Select topics", topics, default=["All"])

    st.markdown("### By Author")
    authors = ["All", "Anuraag Raj", "Anuraganand Sharma", "Deshant Singh"]
    selected_author = st.multiselect("Select authors", authors, default=["All"])

# -- Footer --
st.markdown("---")
footer_html = """
<div style="text-align: center; color: #6B6B6B;">
    <p>For more information about our research, please contact us at <strong>ecols-research@usp.br</strong></p>
    <p>© 2025 ECOLS Research Group | The University of the South Pacific (USP)</p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
