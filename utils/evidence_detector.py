from utils.evidence_rules import evidence_phrases


def detect_evidence_sentences(sentences):

    evidence_sentences = []

    for sentence in sentences:

        for phrase in evidence_phrases:

            if phrase in sentence:
                evidence_sentences.append(sentence)
                break

    return evidence_sentences