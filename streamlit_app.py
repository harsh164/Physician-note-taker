import streamlit as st
from pipeline.entity_extraction import extract_entities
from pipeline.summarization import summarize_text
from pipeline.keyword_extraction import extract_keywords
from pipeline.sentiment_intent import analyze_sentiment_intent
from pipeline.soap_generator import generate_soap_note

st.title("🩺 Physician Notetaker")
text_input = st.text_area("Enter the medical conversation transcript:", height=250)

if st.button("Analyze"):
    if text_input:
        st.subheader("1. Named Entity Extraction")
        st.json(extract_entities(text_input))

        st.subheader("2. Summarized Report")
        st.write(summarize_text(text_input))

        st.subheader("3. Medical Keywords")
        st.write(extract_keywords(text_input))

        st.subheader("4. Sentiment & Intent")
        st.json(analyze_sentiment_intent(text_input))

        st.subheader("5. SOAP Note")
        st.json(generate_soap_note(text_input))
