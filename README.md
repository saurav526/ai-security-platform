# 🛡 AI Security Intelligence Platform

An AI-powered cybersecurity monitoring and threat intelligence platform that combines Machine Learning, Semantic Search, and Large Language Models (LLMs) for real-time security analysis.

The platform is designed to simulate a lightweight Security Operations Center (SOC) system capable of:

- Detecting anomalous network activity
- Searching security logs using semantic AI
- Summarizing alerts using transformer-based language models
- Providing an interactive real-time dashboard

---

# 🚀 Features

## 1. 🚨 Real-Time Anomaly Detection

Detect suspicious network behavior using Machine Learning.

### Capabilities
- Intrusion detection
- Traffic anomaly analysis
- Abnormal behavior detection
- Suspicious request identification

### Model Used
- Isolation Forest (Scikit-Learn)

### Input Features
- Duration
- Source Bytes
- Destination Bytes
- Count
- Server Count

### Output
- NORMAL
- ANOMALY

---

## 2. 🔍 Semantic Security Log Search

Search security logs using semantic similarity instead of exact keyword matching.

### Capabilities
- AI-powered log retrieval
- Similar attack identification
- Threat hunting
- Semantic vector search

### Technologies Used
- Sentence Transformers
- FAISS Vector Database

### Example
Query:
```text
failed login attack

3. 🤖 LLM Alert Summarization

Summarize large security alerts into concise AI-generated insights.

Capabilities
Security incident summarization
Threat explanation
Human-readable alert generation
Model Used
Hugging Face Transformers
BART Summarization Model

                ┌────────────────────┐
                │  Streamlit UI      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   FastAPI Backend  │
                └─────────┬──────────┘
                          │
      ┌───────────────────┼───────────────────┐
      ▼                   ▼                   ▼

┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ ML Detection │   │ Vector Search│   │ LLM Summary  │
└──────────────┘   └──────────────┘   └──────────────┘

🧠 Technologies Used
Category	Technology
Frontend	Streamlit
Backend	FastAPI
Machine Learning	Scikit-Learn
NLP	Sentence Transformers
Vector Search	FAISS
LLM	Hugging Face Transformers
Model Serialization	Joblib
Deployment	Docker / Hugging Face

📂 Project Structure
ai-security-platform/
│
├── backend/
│   ├── app.py
│   ├── model.py
│   ├── train.py
│   ├── vector_store.py
│   ├── llm_summary.py
│   ├── anomaly_model.pkl
│   ├── security_logs.csv
│   └── requirements.txt
│
├── frontend/
│   ├── dashboard.py
│   └── requirements.txt
│
├── Dockerfile
├── docker-compose.yml
└── README.md

⚙ Installation
1. Clone Repository
git clone https://github.com/saurav526/ai-security-platform.git

cd ai-security-platform

