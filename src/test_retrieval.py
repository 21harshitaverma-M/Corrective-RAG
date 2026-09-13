from retriever import load_documents, build_index, retrieve


documents = load_documents()
index = build_index(documents)

query = "What is supervised learning?"

results = retrieve(
    query,
    documents,
    index,
    top_k=2
)

for result in results:
    print("\nSOURCE:", result["source"])
    print("DISTANCE:", result["distance"])
    print("TEXT:", result["text"][:200])