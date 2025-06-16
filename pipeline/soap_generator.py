def generate_soap_note(text):
    return {
        "Subjective": {
            "Chief_Complaint": "Neck and back pain",
            "History_of_Present_Illness": "Patient experienced trauma and ongoing discomfort after an accident."
        },
        "Objective": {
            "Physical_Exam": "Normal range of motion; no visible injuries.",
            "Observations": "Patient appears stable."
        },
        "Assessment": {
            "Diagnosis": "Whiplash injury",
            "Severity": "Mild to moderate"
        },
        "Plan": {
            "Treatment": "Physiotherapy and pain management.",
            "Follow-Up": "Recheck in 2 weeks."
        }
    }
