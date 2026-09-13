import time
import csv

from naive_rag import naive_rag
from crag import corrective_rag


QUESTIONS = [
    {
        "id": 1,
        "question": "What is supervised learning?",
        "expected_source": "local"
    },
    {
        "id": 2,
        "question": "What is natural language processing?",
        "expected_source": "local"
    },
    {
        "id": 3,
        "question": "What is a relational database?",
        "expected_source": "local"
    },
    {
        "id": 4,
        "question": "What is Nvidia's current market capitalization?",
        "expected_source": "web"
    },
    {
        "id": 5,
        "question": "What is the current price of Bitcoin?",
        "expected_source": "web"
    },
    {
        "id": 6,
        "question": "Who is the current president of the United States?",
        "expected_source": "web"
    }
]


results = []


for item in QUESTIONS:

    question = item["question"]

    print("\n" + "=" * 70)
    print(f"QUESTION {item['id']}: {question}")
    print("=" * 70)

    # -------------------------
    # Naive RAG
    # -------------------------

    start = time.perf_counter()

    naive_result = naive_rag(question)

    naive_time = time.perf_counter() - start

    # -------------------------
    # CRAG
    # -------------------------

    start = time.perf_counter()

    crag_result = corrective_rag(question)

    crag_time = time.perf_counter() - start

    print("\nNAIVE RAG ANSWER:")
    print(naive_result["answer"])

    print("\nCRAG SOURCE:", crag_result["source"])

    print("\nCRAG ANSWER:")
    print(crag_result["answer"])

    results.append({
        "id": item["id"],
        "question": question,
        "expected_source": item["expected_source"],
        "naive_time": round(naive_time, 2),
        "crag_time": round(crag_time, 2),
        "crag_source": crag_result["source"],
        "naive_answer": naive_result["answer"],
        "crag_answer": crag_result["answer"]
    })


# Save experiment results
with open(
    "results/experiment_results.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=results[0].keys()
    )

    writer.writeheader()
    writer.writerows(results)


print("\n" + "=" * 70)
print("EXPERIMENT COMPLETE")
print("=" * 70)
print("Results saved to:")
print("results/experiment_results.csv")