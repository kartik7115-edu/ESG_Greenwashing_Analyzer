from transformers import pipeline

# Load FinBERT pipeline
finbert_pipeline = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)


def analyze_sentiment(sentences):

    results = []

    for sentence in sentences:

        try:

            prediction = finbert_pipeline(sentence[:512])[0]

            results.append({
                "sentence": sentence,
                "label": prediction["label"],
                "score": round(prediction["score"], 4)
            })

        except Exception as e:

            results.append({
                "sentence": sentence,
                "label": "ERROR",
                "score": 0
            })

    return results