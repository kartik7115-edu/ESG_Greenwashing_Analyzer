def calculate_greenwashing_risk(
    total_esg_sentences,
    suspicious_sentences,
    evidence_sentences
):

    if total_esg_sentences == 0:
        return 0

    suspicion_ratio = suspicious_sentences / total_esg_sentences

    evidence_ratio = evidence_sentences / total_esg_sentences

    # Weighted scoring
    risk_score = (
        (suspicion_ratio * 70)
        +
        ((1 - evidence_ratio) * 30)
    )

    return round(risk_score, 2)