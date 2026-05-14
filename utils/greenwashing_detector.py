from utils.greenwashing_rules import suspicious_phrases


def detect_suspicious_sentences(sentences):

    flagged_sentences = []

    for sentence in sentences:

        for phrase in suspicious_phrases:

            if phrase in sentence:
                flagged_sentences.append(sentence)
                break

    return flagged_sentences