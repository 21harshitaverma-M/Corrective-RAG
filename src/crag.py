from retriever import load_documents, build_index, retrieve
from grader import grade_document
from web_search import web_search
from generator import generate_answer


def corrective_rag(query: str, top_k: int = 2):

    # 1. Load knowledge base
    documents = load_documents()
    index = build_index(documents)

    # 2. Retrieve candidate documents
    retrieved_documents = retrieve(
        query,
        documents,
        index,
        top_k=top_k
    )

    # 3. Grade retrieved documents
    relevant_documents = []

    for document in retrieved_documents:

        is_relevant = grade_document(
            query,
            document["text"]
        )

        print(
            f"Grading {document['source']}: {is_relevant}"
        )

        if is_relevant:
            relevant_documents.append(document)

    # 4. Decide where the final context comes from
    if relevant_documents:

        print("\nROUTING: LOCAL KNOWLEDGE BASE")

        context = "\n\n".join(
            document["text"]
            for document in relevant_documents
        )

        source = "local"

    else:

        print("\nROUTING: WEB FALLBACK")

        web_results = web_search(query)

        context = "\n\n".join(
            result["content"]
            for result in web_results
        )

        source = "web"

    # 5. Generate grounded answer
    answer = generate_answer(
        query,
        context
    )

    return {
        "answer": answer,
        "source": source,
        "context": context
    }