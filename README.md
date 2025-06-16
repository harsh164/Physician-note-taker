 Physician Notetaker

An AI-powered tool that transforms medical conversation transcripts into structured SOAP notes using NLP techniques.

Features

- Summarizes transcripts
- Extracts medical entities and keywords
- Analyzes sentiment & intent
- Generates SOAP notes (Subjective, Objective, Assessment, Plan)

Methodology

Summarization:DistilBART (`sshleifer/distilbart-cnn-12-6`)
Entity Extraction:SciSpaCy (`en_core_sci_sm`)
Sentiment Analysis:VADER
Keywords: RAKE
SOAP Generator:Template-based logic

Setup
git clone https://github.com/your-username/physician-notetaker.git
cd physician-notetaker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz
streamlit run streamlit_app.py
