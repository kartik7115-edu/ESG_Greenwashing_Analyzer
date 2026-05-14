from utils.esg_keywords import (
    environment_keywords,
    social_keywords,
    governance_keywords
)


def count_keywords(text, keywords):
    count = 0

    for keyword in keywords:
        count += text.count(keyword)

    return count


def calculate_esg_scores(text):

    environmental_score = count_keywords(text, environment_keywords)

    social_score = count_keywords(text, social_keywords)

    governance_score = count_keywords(text, governance_keywords)

    return {
        "Environmental": environmental_score,
        "Social": social_score,
        "Governance": governance_score
    }