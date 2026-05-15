# 🌱 ESG Greenwashing Analyzer

An AI-powered NLP application that analyzes ESG (Environmental, Social, and Governance) reports to detect potential greenwashing risks using Natural Language Processing and sustainability intelligence.

---

## 🚀 Project Overview

Companies publish ESG and sustainability reports to showcase their environmental and social initiatives. However, many reports contain vague, promotional, or misleading claims without measurable evidence.

This project helps identify:
- ⚠️ Potential greenwashing language
- ✅ Evidence-backed sustainability disclosures
- 📊 ESG transparency metrics
- 🎯 Greenwashing risk scores

The application extracts text from ESG PDF reports, processes the content using NLP techniques, and generates an interactive ESG risk analysis dashboard.

---

## ✨ Features

### 📄 PDF ESG Report Analysis
Upload sustainability or ESG reports in PDF format for automated analysis.

### 🧠 NLP-Based ESG Detection
Extracts and analyzes ESG-related statements from reports.

### ⚠️ Suspicious Claim Detection
Flags vague sustainability claims such as:
- "We aim to..."
- "We are committed to..."
- "Working toward..."
- "Striving to..."

### ✅ Evidence-Based Claim Detection
Identifies measurable ESG disclosures including:
- Percentages
- Carbon emission metrics
- Renewable energy statistics
- Quantifiable sustainability outcomes

### 🎯 Greenwashing Risk Scoring
Generates a risk score (0–100) based on:
- Promotional ESG language
- Lack of measurable evidence
- Transparency indicators

### 📊 Interactive Dashboard
Built using Streamlit and Plotly for:
- ESG analytics
- Risk visualization
- Charts and graphs
- Claim categorization

---

# 🏗️ Project Architecture

```text
PDF ESG Report
        ↓
Text Extraction
        ↓
Text Cleaning
        ↓
Sentence Tokenization
        ↓
ESG Statement Detection
        ↓
Suspicious Claim Detection
        ↓
Evidence Detection
        ↓
Risk Scoring Engine
        ↓
Interactive Dashboard
```

---

# 🛠️ Tech Stack

## Programming Language
- Python

## NLP & Text Processing
- NLTK
- Regex
- PyPDF2

## Data Visualization
- Plotly
- Pandas

## Dashboard
- Streamlit

## ESG Intelligence
- Custom Greenwashing Risk Engine

---

# 📂 Project Structure

```text
esg-greenwashing-analyzer/
│
├── app/
│   └── streamlit_app.py
│
├── utils/
│   ├── pdf_extractor.py
│   ├── text_cleaner.py
│   ├── sentence_extractor.py
│   ├── greenwashing_detector.py
│   ├── evidence_detector.py
│   ├── risk_scoring.py
│   └── risk_interpreter.py
│
├── sample_reports/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/esg-greenwashing-analyzer.git
```

---

## 2️⃣ Navigate to Project

```bash
cd esg-greenwashing-analyzer
```

---

## 3️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
```

### Activate Virtual Environment
```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app/streamlit_app.py
```

---

# 📊 Sample Output

The dashboard provides:

- ESG sentence count
- Suspicious claim count
- Evidence-based claim count
- Greenwashing risk score
- ESG analytics charts
- Risk interpretation

---

# 🧪 Example Use Cases

- ESG transparency analysis
- Sustainability reporting assessment
- Corporate ESG benchmarking
- Greenwashing risk research
- Climate disclosure evaluation
- ESG consulting analytics

---

# 📈 Future Improvements

- 🤖 FinBERT Integration
- 🧠 Transformer-based ESG classification
- 📑 Automated ESG report summarization
- 🌍 Multi-company ESG comparison
- 📊 Historical ESG trend analysis
- 📥 Downloadable ESG assessment reports
- ☁️ Cloud deployment support

---

# 🎯 Why This Project Matters

Greenwashing has become a major issue in sustainability reporting. This project demonstrates how AI and NLP can help improve:
- ESG transparency
- Sustainability accountability
- Data-driven ESG evaluation
- Responsible corporate reporting

---

# 🌐 Live Demo

Try the deployed application here:

👉 [ESG Greenwashing Analyzer Live App](https://your-deployment-link.streamlit.app)

---


# 👨‍💻 Author

Kartik

Engineering Student | Data Science Enthusiast | AI & Sustainability Explorer

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub and connect with me on LinkedIn!

---
