import streamlit as st

st.markdown("""
<style>
    .paper-card {
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 12px 0 rgba(0,0,0,0.1);
        margin-bottom: 30px;
        background-color: #FFFFFF;
        border-left: 5px solid #4B8BBE;
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
    .download-btn {
        background-color: #4B8BBE;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        cursor: pointer;
    }
</style>

<div class='paper-card'>
    <h2 class='paper-title'>AI-Based Sentiment Analysis for Mental Health Assessment</h2>
    <p class='paper-authors'>Anuraganand Sharma, Anuraag Raj, Deshant Singh</p>
    
    <div class='paper-meta'>
        <span class='paper-meta-item'>📅 2020</span>
        <span class='paper-meta-item'>🏷️ <span class='tag'>Sentiment Analysis</span> <span class='tag'>AI</span> <span class='tag'>Mental Health</span></span>
        <span class='paper-meta-item'>📊 Springer</span>
    </div>
    
    <div class='paper-abstract'>
        <strong>Abstract:</strong> This research explores advanced sentiment analysis techniques for mental health assessment in digital 
        communication. We propose a hybrid model combining lexicon-based approaches with deep learning, capable of detecting subtle 
        emotional cues indicative of mental health conditions. The system achieves 85% precision in identifying high-risk cases across 
        multiple languages.
    </div>
    
    <a href="https://link.springer.com/article/10.1007/s42485-020-00044-9" target="_blank">
        <button class='download-btn'>
            📄 Read Full Paper
        </button>
    </a>
</div>
""", unsafe_allow_html=True)