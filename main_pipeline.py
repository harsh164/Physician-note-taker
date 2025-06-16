from pipeline.entity_extraction import extract_entities
from pipeline.summarization import summarize_text
from pipeline.keyword_extraction import extract_keywords
from pipeline.sentiment_intent import analyze_sentiment_intent
from pipeline.soap_generator import generate_soap_note

sample_input = """I hit my head on the steering wheel on September 1st. I could feel pain in my neck and back.
I'm doing better, but I still have some discomfort now and then. They said it was a whiplash injury.
They didn't do X-rays. They just gave advice. Took painkillers and had ten sessions of physiotherapy."""

print("\n--- Named Entity Extraction ---")
print(extract_entities(sample_input))

print("\n--- Summarized Report ---")
print(summarize_text(sample_input))

print("\n--- Medical Keywords ---")
print(extract_keywords(sample_input))

print("\n--- Sentiment & Intent ---")
print(analyze_sentiment_intent(sample_input))

print("\n--- SOAP Note ---")
print(generate_soap_note(sample_input))
