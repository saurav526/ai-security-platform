from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)


def summarize_alert(alert_text):
    result = summarizer(
        alert_text,
        max_length=60,
        min_length=20,
        do_sample=False
    )

    return result[0]['summary_text']