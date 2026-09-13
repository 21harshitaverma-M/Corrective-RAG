import csv
from statistics import mean


with open(
    "results/experiment_results.csv",
    "r",
    encoding="utf-8"
) as file:

    rows = list(csv.DictReader(file))


# -------------------------
# Routing accuracy
# -------------------------

correct_routes = sum(
    row["expected_source"] == row["crag_source"]
    for row in rows
)

routing_accuracy = (
    correct_routes / len(rows)
) * 100


# -------------------------
# Average latency
# -------------------------

average_naive_time = mean(
    float(row["naive_time"])
    for row in rows
)

average_crag_time = mean(
    float(row["crag_time"])
    for row in rows
)


# -------------------------
# Print summary
# -------------------------

print("=" * 60)
print("EXPERIMENT SUMMARY")
print("=" * 60)

print(f"\nTotal questions: {len(rows)}")

print(
    f"CRAG routing accuracy: "
    f"{routing_accuracy:.2f}%"
)

print(
    f"Average Naive RAG latency: "
    f"{average_naive_time:.2f} seconds"
)

print(
    f"Average CRAG latency: "
    f"{average_crag_time:.2f} seconds"
)

print("\nROUTING DETAILS:")

for row in rows:

    print(
        f"Q{row['id']}: "
        f"expected={row['expected_source']}, "
        f"actual={row['crag_source']}"
    )