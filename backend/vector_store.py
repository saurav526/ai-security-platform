import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

security_logs = [
    "Multiple failed login attempts from IP 192.168.1.2",
    "SQL injection attempt detected",
    "DDoS traffic spike detected",
    "Normal user login activity"
]

embeddings = model.encode(security_logs)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype('float32'))


def semantic_search(query, top_k=2):
    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype('float32'),
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(security_logs[idx])

    return results