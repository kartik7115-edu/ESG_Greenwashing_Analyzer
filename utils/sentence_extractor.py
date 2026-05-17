import nltk
from nltk.tokenize import sent_tokenize

# Download tokenizer resources
nltk.download("punkt")
nltk.download("punkt_tab")

ESG_KEYWORDS = [
    "sustainability",
    "environment",
    "climate",
    "carbon",
    "emissions",
    "renewable",
    "recycled",
    "energy",
    "waste",
    "water",
    "greenhouse",
    "esg",
    "net zero",
    "biodiversity",
    "social",
    "governance"
]


def extract_esg_sentences(text):

    sentences = sent_tokenize(text)

    esg_sentences = []

    for sentence in sentences:

        sentence_lower = sentence.lower()

        if any(keyword in sentence_lower for keyword in ESG_KEYWORDS):

            esg_sentences.append(sentence)

    return esg_sentences
