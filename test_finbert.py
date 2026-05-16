from utils.finbert_analyzer import analyze_sentiment

sample_sentences = [

    "We aim to become carbon neutral by 2030.",

    "Our emissions reduced by 60 percent since 2015.",

    "We are committed to sustainability initiatives."
]

results = analyze_sentiment(sample_sentences)

for result in results:

    print(result)