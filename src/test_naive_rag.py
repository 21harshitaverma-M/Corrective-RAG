from naive_rag import naive_rag


query = "What is supervised learning?"

result = naive_rag(query)

print("=" * 50)
print("NAIVE RAG")
print("=" * 50)

print("\nRETRIEVED DOCUMENTS:")

for document in result["documents"]:
    print("-", document["source"])

print("\nANSWER:")
print(result["answer"])