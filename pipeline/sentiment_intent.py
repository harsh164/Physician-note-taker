from transformers import pipeline

classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)

def analyze_sentiment_intent(text):
    results = classifier(text)[0]
    sorted_res = sorted(results, key=lambda x: x['score'], reverse=True)
    return {
        "Sentiment": sorted_res[0]['label'],
        "Intent": "Seeking reassurance" if "pain" in text.lower() else "General"
    }
