import csv


EXPECTED_KEYWORDS = {
    1: ["supervised learning", "labeled", "classification", "regression"],
    2: ["natural language processing", "human language"],
    3: ["relational database", "tables", "sql"],
    4: ["nvidia", "market capitalization"],
    5: ["bitcoin"],
    6: ["donald", "trump"]
}


with open(
    "results/experiment_results.csv",
    "r",
    encoding="utf-8"
) as file:

    rows = list(csv.DictReader(file))


print("=" * 70)
print("ANSWER EVALUATION")
print("=" * 70)

total_naive_score = 0
total_crag_score = 0
total_keywords = 0


for row in rows:

    question_id = int(row["id"])
    keywords = EXPECTED_KEYWORDS[question_id]

    naive_answer = row["naive_answer"].lower()
    crag_answer = row["crag_answer"].lower()

    naive_matches = sum(
        keyword in naive_answer
        for keyword in keywords
    )

    crag_matches = sum(
        keyword in crag_answer
        for keyword in keywords
    )

    total_naive_score += naive_matches
    total_crag_score += crag_matches
    total_keywords += len(keywords)

    print(f"\nQ{question_id}: {row['question']}")

    print(
        f"Naive RAG: "
        f"{naive_matches}/{len(keywords)} keywords"
    )

    print(
        f"CRAG:      "
        f"{crag_matches}/{len(keywords)} keywords"
    )


print("\n" + "=" * 70)
print("OVERALL KEYWORD COVERAGE")
print("=" * 70)

naive_coverage = (
    total_naive_score / total_keywords
) * 100

crag_coverage = (
    total_crag_score / total_keywords
) * 100

print(
    f"\nNaive RAG keyword coverage: "
    f"{naive_coverage:.2f}%"
)

print(
    f"CRAG keyword coverage: "
    f"{crag_coverage:.2f}%"
)

print("\nNOTE:")
print(
    "Keyword coverage is a lightweight evaluation metric and "
    "should not be interpreted as full factual accuracy."
)