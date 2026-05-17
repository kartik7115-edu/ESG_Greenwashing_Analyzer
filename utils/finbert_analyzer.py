from transformers import pipeline

# Lazy-loaded pipeline
finbert_pipeline = None


def get_pipeline():

    global finbert_pipeline

    if finbert_pipeline is None:

        finbert_pipeline = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert"
        )

    return finbert_pipeline


def analyze_sentiment(sentences):

    pipe = get_pipeline()

    results = []

    for sentence in sentences:

        try:

            prediction = pipe(sentence[:512])[0]

            results.append({
                "sentence": sentence,
                "label": prediction["label"],
                "score": round(prediction["score"], 3)
            })

        except Exception:

            results.append({
                "sentence": sentence,
                "label": "ERROR",
                "score": 0
            })

    return results
