from pathlib import Path

import faiss
import numpy as np

from embeddings import get_embedding


KNOWLEDGE_BASE_PATH = Path(__file__).parent.parent / "data" / "knowledge_base"


def load_documents():
    documents = []

    for file_path in KNOWLEDGE_BASE_PATH.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "text": text,
            "source": file_path.name
        })

    return documents


def build_index(documents):
    embeddings = [
        get_embedding(document["text"])
        for document in documents
    ]

    matrix = np.array(embeddings, dtype="float32")

    index = faiss.IndexFlatL2(matrix.shape[1])
    index.add(matrix)

    return index


def retrieve(query, documents, index, top_k=2):
    query_embedding = np.array(
        [get_embedding(query)],
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_id in zip(distances[0], indices[0]):
        if index_id != -1:
            results.append({
                "text": documents[index_id]["text"],
                "source": documents[index_id]["source"],
                "distance": float(distance)
            })

    return results