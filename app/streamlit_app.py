import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from utils.finbert_analyzer import analyze_sentiment
from utils.pdf_extractor import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.sentence_extractor import extract_esg_sentences
from utils.greenwashing_detector import detect_suspicious_sentences
from utils.evidence_detector import detect_evidence_sentences
from utils.risk_scoring import calculate_greenwashing_risk
from utils.risk_interpreter import interpret_risk


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="ESG Greenwashing Analyzer",
    page_icon="🌱",
    layout="wide"
)


# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1, h2, h3 {
    color: white;
}

.metric-card {
    padding: 20px;
    border-radius: 12px;
    background-color: #1E1E1E;
    color: white;
}

.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# TITLE
# -----------------------------------

st.title("🌱 ESG Greenwashing Analyzer")

st.markdown("""
Analyze ESG reports for potential greenwashing risk using NLP and sustainability intelligence.
""")


# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload ESG Report PDF",
    type=["pdf"]
)


# -----------------------------------
# MAIN PIPELINE
# -----------------------------------

if uploaded_file is not None:

    # Save uploaded PDF temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract text from PDF
    raw_text = extract_text_from_pdf("temp.pdf")

    # Clean extracted text
    cleaned_text = clean_text(raw_text)

    # Extract ESG-related sentences
    esg_sentences = extract_esg_sentences(cleaned_text)

    # Detect suspicious ESG claims
    suspicious_sentences = detect_suspicious_sentences(
        esg_sentences
    )

    # Detect evidence-based ESG claims
    evidence_sentences = detect_evidence_sentences(
        esg_sentences
    )

    # FinBERT sentiment analysis
    sentiment_results = analyze_sentiment(
        esg_sentences[:30]
    )

    # Calculate risk score
    risk_score = calculate_greenwashing_risk(
        total_esg_sentences=len(esg_sentences),
        suspicious_sentences=len(suspicious_sentences),
        evidence_sentences=len(evidence_sentences)
    )

    # Risk interpretation
    risk_level = interpret_risk(risk_score)

    # Sentiment counts
    positive_count = sum(
        1 for r in sentiment_results
        if r["label"].lower() == "positive"
    )

    negative_count = sum(
        1 for r in sentiment_results
        if r["label"].lower() == "negative"
    )

    neutral_count = sum(
        1 for r in sentiment_results
        if r["label"].lower() == "neutral"
    )

    # -----------------------------------
    # METRICS
    # -----------------------------------

    st.divider()

    st.header("📊 ESG Analysis Results")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "ESG Sentences",
        len(esg_sentences)
    )

    col2.metric(
        "Suspicious Claims",
        len(suspicious_sentences)
    )

    col3.metric(
        "Evidence Claims",
        len(evidence_sentences)
    )

    col4.metric(
        "Risk Score",
        f"{risk_score}/100"
    )

    # -----------------------------------
    # RISK INTERPRETATION
    # -----------------------------------

    st.subheader("🧠 Risk Interpretation")

    if risk_score < 20:
        st.success(risk_level)

    elif risk_score < 50:
        st.warning(risk_level)

    else:
        st.error(risk_level)

    # -----------------------------------
    # RISK GAUGE
    # -----------------------------------

    st.subheader("🎯 Greenwashing Risk Gauge")

    gauge_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text': "Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkred"},
            'steps': [
                {'range': [0, 20], 'color': "green"},
                {'range': [20, 50], 'color': "yellow"},
                {'range': [50, 100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(
        gauge_fig,
        use_container_width=True
    )

    # -----------------------------------
    # ESG OVERVIEW BAR CHART
    # -----------------------------------

    st.subheader("📈 ESG Analysis Overview")

    chart_data = pd.DataFrame({
        "Category": [
            "ESG Sentences",
            "Suspicious Claims",
            "Evidence Claims"
        ],
        "Count": [
            len(esg_sentences),
            len(suspicious_sentences),
            len(evidence_sentences)
        ]
    })

    fig = px.bar(
        chart_data,
        x="Category",
        y="Count",
        text="Count",
        title="Distribution of ESG Insights"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -----------------------------------
    # FINBERT SENTIMENT ANALYSIS
    # -----------------------------------

    st.subheader("🤖 FinBERT ESG Sentiment Analysis")

    sentiment_df = pd.DataFrame({
        "Sentiment": [
            "Positive",
            "Neutral",
            "Negative"
        ],
        "Count": [
            positive_count,
            neutral_count,
            negative_count
        ]
    })

    sentiment_fig = px.pie(
        sentiment_df,
        names="Sentiment",
        values="Count",
        title="FinBERT ESG Sentiment Distribution"
    )

    st.plotly_chart(
        sentiment_fig,
        use_container_width=True
    )

    # -----------------------------------
    # PIE CHART
    # -----------------------------------

    st.subheader("🧩 ESG Claim Composition")

    pie_data = pd.DataFrame({
        "Type": [
            "Suspicious Claims",
            "Evidence Claims"
        ],
        "Count": [
            len(suspicious_sentences),
            len(evidence_sentences)
        ]
    })

    pie_fig = px.pie(
        pie_data,
        names="Type",
        values="Count",
        title="Claim Composition"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

    # -----------------------------------
    # SUSPICIOUS CLAIMS
    # -----------------------------------

    st.divider()

    st.subheader("⚠️ Flagged Suspicious Claims")

    if suspicious_sentences:

        for sentence in suspicious_sentences[:15]:
            st.warning(sentence)

    else:
        st.success(
            "No suspicious ESG claims detected."
        )

    # -----------------------------------
    # EVIDENCE CLAIMS
    # -----------------------------------

    st.subheader("✅ Evidence-Based ESG Statements")

    if evidence_sentences:

        for sentence in evidence_sentences[:15]:
            st.success(sentence)

    else:
        st.info(
            "No evidence-based ESG statements detected."
        )

    # -----------------------------------
    # FINBERT SENTENCE ANALYSIS
    # -----------------------------------

    st.subheader("🧠 FinBERT Sentence Intelligence")

    for result in sentiment_results[:10]:

        sentence = result["sentence"]
        label = result["label"]
        score = result["score"]

        if label.lower() == "positive":

            st.success(
                f"{label.upper()} ({score}) → {sentence}"
            )

        elif label.lower() == "negative":

            st.error(
                f"{label.upper()} ({score}) → {sentence}"
            )

        else:

            st.info(
                f"{label.upper()} ({score}) → {sentence}"
            )

    # -----------------------------------
    # RAW ESG SENTENCES
    # -----------------------------------

    with st.expander("📄 View Extracted ESG Sentences"):

        for sentence in esg_sentences[:50]:
            st.write(sentence)

    # -----------------------------------
    # SUMMARY
    # -----------------------------------

    st.divider()

    st.subheader("📝 ESG Assessment Summary")

    st.markdown(f"""
### Final Assessment

- Total ESG Statements Analyzed: **{len(esg_sentences)}**
- Suspicious ESG Claims: **{len(suspicious_sentences)}**
- Evidence-Based Statements: **{len(evidence_sentences)}**
- Greenwashing Risk Score: **{risk_score}/100**
- Risk Category: **{risk_level}**

### Interpretation

This ESG report contains a combination of:
- sustainability commitments
- operational disclosures
- measurable environmental metrics
- future-oriented ESG initiatives

The detected risk score reflects the balance between:
- vague/promotional ESG language
- evidence-backed sustainability disclosures
""")

else:

    st.info(
        "Upload an ESG PDF report to begin analysis."
    )