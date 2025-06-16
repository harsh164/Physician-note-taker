import re

def extract_entities(text):
    symptoms = re.findall(r'(?i)(pain|discomfort|injury|headache|back pain|neck pain)', text)
    diagnosis = "Whiplash injury" if "whiplash" in text.lower() else "Unknown"
    treatment = [s for s in re.findall(r'(?i)(painkillers|physiotherapy|x-ray|therapy)', text)]
    return {
        "Symptoms": list(set(symptoms)),
        "Diagnosis": diagnosis,
        "Treatment": treatment,
        "Prognosis": None
    }
