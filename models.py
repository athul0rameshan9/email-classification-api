def classify_email(text: str) -> str:
    from transformers import pipeline

    classifier = pipeline("text-classification", model="./bert-email-classifier", tokenizer="./bert-email-classifier")
    prediction = classifier(text, truncation=True, max_length=512)
    print(prediction)  # → [{'label': 'LABEL_0', 'score': 0.99}]


    dict_map  = {0: 'Change', 1: 'Incident', 2: 'Problem', 3: 'Request'}
    label_index = int(prediction[0]['label'].split('_')[-1])
    mapped_label = dict_map[label_index]
    return mapped_label    # → 'Problem'
