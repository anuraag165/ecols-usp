import streamlit as st
import pandas as pd

st.title("📄 Research Papers")

df = pd.read_csv("data/papers.csv")

for _, row in df.iterrows():
    st.subheader(row['Title'])
    st.markdown(f"**Authors:** {row['Authors']}")
    st.markdown(f"**Year:** {row['Year']}")
    st.markdown(f"**Abstract:** {row['Abstract']}")
    st.markdown(f"[Read Full Paper]({row['Link']})")
    st.markdown("---")
