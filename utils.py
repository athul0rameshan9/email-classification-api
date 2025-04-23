import re
import spacy

nlp = spacy.load("en_core_web_sm")

# Regex patterns
PATTERNS = {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "phone_number": r"\b(\+91[\s-]?)?[6-9]\d{9}\b",
    "dob": r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    "aadhar_num": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,19}\b",
    "cvv_no": r"\b\d{3,4}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])[/\-]\d{2,4}\b"
}

def mask_pii(text):
    entities = []
    masked_text = text

    # Mask via Regex
    for label, pattern in PATTERNS.items():
        for match in re.finditer(pattern, text):
            start, end = match.start(), match.end()
            original = text[start:end]
            masked_text = masked_text.replace(original, f"[{label}]")
            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": original
            })

    # Mask full name via spaCy NER
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            start, end = ent.start_char, ent.end_char
            original = ent.text
            masked_text = masked_text.replace(original, "[full_name]")
            entities.append({
                "position": [start, end],
                "classification": "full_name",
                "entity": original
            })

    return masked_text, entities




