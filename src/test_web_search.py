from web_search import web_search


query = "What is the current market capitalization of Nvidia?"

results = web_search(query)


for result in results:
    print("\nTITLE:", result["title"])
    print("URL:", result["url"])
    print("CONTENT:", result["content"][:300])