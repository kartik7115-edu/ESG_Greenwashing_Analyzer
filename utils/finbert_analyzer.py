from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_pipeline():

    return pipeline(
        "sentiment-analysis",
        model="ProsusAI/finbert",
        framework="pt"
    )


def analyze_sentiment(sentences):

    pipe = load_pipeline()

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
