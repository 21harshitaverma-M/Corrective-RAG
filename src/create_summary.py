import csv


with open(
    "results/experiment_results.csv",
    "r",
    encoding="utf-8"
) as file:

    rows = list(csv.DictReader(file))


print("=" * 70)
print("NAIVE RAG VS CRAG — EXPERIMENT RESULTS")
print("=" * 70)

print(
    f"\n{'Q':<4}"
    f"{'Expected':<12}"
    f"{'CRAG Route':<12}"
    f"{'Naive(s)':<12}"
    f"{'CRAG(s)':<12}"
)

print("-" * 52)

for row in rows:

    print(
        f"{row['id']:<4}"
        f"{row['expected_source']:<12}"
        f"{row['crag_source']:<12}"
        f"{row['naive_time']:<12}"
        f"{row['crag_time']:<12}"
    )