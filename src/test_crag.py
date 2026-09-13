from crag import corrective_retrieve


print("=" * 50)
print("TEST 1: LOCAL KNOWLEDGE")
print("=" * 50)

query = "What is supervised learning?"

result = corrective_retrieve(query)

print("\nFINAL SOURCE:", result["source"])

for document in result["documents"]:
    print("\nDOCUMENT:")
    print(document["text"][:300])


print("\n" + "=" * 50)
print("TEST 2: WEB FALLBACK")
print("=" * 50)

query = "What is Nvidia's current market capitalization?"

result = corrective_retrieve(query)

print("\nFINAL SOURCE:", result["source"])

for document in result["documents"]:
    print("\nTITLE:", document.get("title"))
    print("URL:", document.get("url"))
    print("CONTENT:", document.get("content", "")[:300])