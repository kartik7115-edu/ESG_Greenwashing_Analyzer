from utils.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text

pdf_path = "reports\Apple_Environmental_Progress_Report_2026.pdf"

# Extract text
raw_text = extract_text_from_pdf(pdf_path)

# Clean text
cleaned_text = clean_text(raw_text)

# Print first 3000 characters
#print(cleaned_text[:3000])

from utils.esg_scoring import calculate_esg_scores

scores = calculate_esg_scores(cleaned_text)

print(scores)

from utils.sentence_extractor import extract_esg_sentences

esg_sentences = extract_esg_sentences(cleaned_text)

print("\nTOTAL ESG SENTENCES:", len(esg_sentences))

print("\nFIRST 10 ESG SENTENCES:\n")

#for sentence in esg_sentences[:10]:
 #   print("-", sentence)


from utils.greenwashing_detector import detect_suspicious_sentences

flagged_sentences = detect_suspicious_sentences(esg_sentences)

print("\nTOTAL FLAGGED SENTENCES:", len(flagged_sentences))

print("\nFLAGGED SENTENCES:\n")

for sentence in flagged_sentences[:20]:
    print("\n -", sentence)


from utils.evidence_detector import detect_evidence_sentences

evidence_sentences = detect_evidence_sentences(esg_sentences)

print("\n##TOTAL EVIDENCE SENTENCES:", len(evidence_sentences))

print("\n##EVIDENCE-BASED SENTENCES:\n")

for sentence in evidence_sentences[:20]:
    print("-", sentence)


from utils.risk_scoring import calculate_greenwashing_risk

risk_score = calculate_greenwashing_risk(
    total_esg_sentences=len(esg_sentences),
    suspicious_sentences=len(flagged_sentences),
    evidence_sentences=len(evidence_sentences)
)

print("\nGREENWASHING RISK SCORE:")
print(risk_score)

from utils.risk_interpreter import interpret_risk

risk_level = interpret_risk(risk_score)

print("\nRISK LEVEL:")
print(risk_level)