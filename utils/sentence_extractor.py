import re

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

    # Simple sentence splitting
    sentences = re.split(r'(?<=[.!?])\s+', text)

    esg_sentences = []

    for sentence in sentences:

        sentence_lower = sentence.lower()

        if any(keyword in sentence_lower for keyword in ESG_KEYWORDS):

            esg_sentences.append(sentence.strip())

    return esg_sentences
