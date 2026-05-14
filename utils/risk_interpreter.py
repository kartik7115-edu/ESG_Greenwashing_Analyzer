def interpret_risk(score):

    if score < 20:
        return "Low Greenwashing Risk"

    elif score < 50:
        return "Moderate Greenwashing Risk"

    else:
        return "High Greenwashing Risk"