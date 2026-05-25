import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Security Intelligence Platform",
    page_icon="🛡",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🛡 AI Security Intelligence Platform")

st.markdown(
    "Real-Time Cybersecurity Monitoring using Machine Learning, "
    "Semantic Search, and LLM-Based Alert Analysis"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Select Module",
    [
        "Anomaly Detection",
        "Semantic Search",
        "LLM Alert Summary"
    ]
)

# ===================================================
# ANOMALY DETECTION
# ===================================================

if option == "Anomaly Detection":

    st.header("🚨 Real-Time Intrusion Detection")

    st.markdown(
        "Enter network traffic features to detect suspicious activity."
    )

    col1, col2 = st.columns(2)

    with col1:
        duration = st.number_input(
            "Duration",
            min_value=0.0,
            value=10.0
        )

        src_bytes = st.number_input(
            "Source Bytes",
            min_value=0.0,
            value=100.0
        )

        dst_bytes = st.number_input(
            "Destination Bytes",
            min_value=0.0,
            value=200.0
        )

    with col2:
        count = st.number_input(
            "Count",
            min_value=0.0,
            value=5.0
        )

        srv_count = st.number_input(
            "Server Count",
            min_value=0.0,
            value=3.0
        )

    if st.button("Detect Threat"):

        payload = {
            "duration": duration,
            "src_bytes": src_bytes,
            "dst_bytes": dst_bytes,
            "count": count,
            "srv_count": srv_count
        }

        try:
            response = requests.post(
                f"{API_URL}/predict",
                json=payload
            )

            result = response.json()["prediction"]

            st.subheader("Detection Result")

            if result == "ANOMALY":
                st.error("⚠ Threat Detected: ANOMALY")

                st.warning(
                    "Suspicious network behavior detected. "
                    "Possible intrusion or attack pattern."
                )

            else:
                st.success("✅ Status: NORMAL")

                st.info(
                    "Traffic appears normal and safe."
                )

        except Exception as e:
            st.error(f"Error: {e}")

# ===================================================
# SEMANTIC SEARCH
# ===================================================

elif option == "Semantic Search":

    st.header("🔍 AI Security Log Search")

    st.markdown(
        "Search security logs using semantic vector similarity."
    )

    query = st.text_input(
        "Search Logs",
        placeholder="Example: failed login attack"
    )

    if st.button("Search"):

        try:
            response = requests.post(
                f"{API_URL}/search",
                json={"query": query}
            )

            results = response.json()["results"]

            st.subheader("Search Results")

            if len(results) == 0:
                st.warning("No matching logs found.")

            for i, result in enumerate(results, start=1):

                st.markdown(
                    f"""
                    ### Result {i}
                    {result}
                    """
                )

        except Exception as e:
            st.error(f"Error: {e}")

# ===================================================
# LLM ALERT SUMMARY
# ===================================================

elif option == "LLM Alert Summary":

    st.header("🤖 AI Alert Summarization")

    st.markdown(
        "Paste a large security alert to generate an AI summary."
    )

    alert = st.text_area(
        "Paste Security Alert",
        height=200,
        placeholder="Paste long security alert text here..."
    )

    if st.button("Generate Summary"):

        try:
            response = requests.post(
                f"{API_URL}/summarize",
                json={"alert": alert}
            )

            summary = response.json()["summary"]

            st.subheader("AI Generated Summary")

            st.success(summary)

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown(
    "Built using FastAPI, Streamlit, FAISS, "
    "Sentence Transformers, and Machine Learning"
)