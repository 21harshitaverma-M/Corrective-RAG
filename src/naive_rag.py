from retriever import load_documents, build_index, retrieve
from generator import generate_answer


def naive_rag(query: str, top_k: int = 2):

    documents = load_documents()
    index = build_index(documents)

    retrieved_documents = retrieve(
        query,
        documents,
        index,
        top_k=top_k
    )

    context = "\n\n".join(
        document["text"]
        for document in retrieved_documents
    )

    answer = generate_answer(
        query,
        context
    )

    return {
        "answer": answer,
        "documents": retrieved_documents
    }