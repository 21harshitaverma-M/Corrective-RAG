from crag import corrective_rag


print("=" * 60)
print("CRAG TEST 1 — LOCAL KNOWLEDGE")
print("=" * 60)

result = corrective_rag(
    "What is supervised learning?"
)

print("\nSOURCE:", result["source"])
print("\nANSWER:")
print(result["answer"])


print("\n" + "=" * 60)
print("CRAG TEST 2 — WEB FALLBACK")
print("=" * 60)

result = corrective_rag(
    "What is Nvidia's current market capitalization?"
)

print("\nSOURCE:", result["source"])
print("\nANSWER:")
print(result["answer"])