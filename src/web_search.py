from tavily import TavilyClient

from config import TAVILY_API_KEY


client = TavilyClient(api_key=TAVILY_API_KEY)


def web_search(query: str, max_results: int = 3):
    response = client.search(
        query=query,
        max_results=max_results
    )

    results = []

    for result in response["results"]:
        results.append({
            "title": result["title"],
            "url": result["url"],
            "content": result["content"]
        })

    return results