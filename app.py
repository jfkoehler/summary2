#in a virtual enviornment using
# pipenv (pip install pipenv)
# pipenv shell -- creates new venv
# 
import streamlit as st
from transformers import pipeline

pipe = pipeline("summarization", model="facebook/bart-large-cnn")

article = st.text_area("Input text to be summarized")
max_len = st.slider("Max Length of Summary", 50, 200)
min_len = st.slider("Minimum Length of Summary", 5, 50)
output = pipe(article, max_length=max_len, min_length=min_len, do_sample=False)

st.write("Here is the summary:")

st.write(output)