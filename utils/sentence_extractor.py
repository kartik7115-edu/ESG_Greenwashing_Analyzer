import nltk
from nltk.tokenize import sent_tokenize

from utils.esg_keywords import (
    environment_keywords,
    social_keywords,
    governance_keywords
)


all_keywords = (
    environment_keywords
    + social_keywords
    + governance_keywords
)


def extract_esg_sentences(text):

    sentences = sent_tokenize(text)

    esg_sentences = []

    for sentence in sentences:

        for keyword in all_keywords:

            if keyword in sentence:
                esg_sentences.append(sentence)
                break

    return esg_sentences