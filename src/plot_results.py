import pandas as pd
import matplotlib.pyplot as plt

# Load experiment results
results = pd.read_csv("results/experiment_results.csv")

# --------------------------------
# 1. Latency comparison
# --------------------------------

naive_latency = results["naive_time"].mean()
crag_latency = results["crag_time"].mean()

plt.figure(figsize=(7, 5))

plt.bar(
    ["Naive RAG", "CRAG"],
    [naive_latency, crag_latency]
)

plt.ylabel("Average Latency (seconds)")
plt.title("Average Response Latency: Naive RAG vs CRAG")

plt.tight_layout()

plt.savefig("results/latency_comparison.png")
plt.close()


# --------------------------------
# 2. CRAG routing accuracy
# --------------------------------

correct_routes = (
    results["expected_source"] == results["crag_source"]
).sum()

total_questions = len(results)

routing_accuracy = (
    correct_routes / total_questions
) * 100

plt.figure(figsize=(7, 5))

plt.bar(
    ["CRAG Routing Accuracy"],
    [routing_accuracy]
)

plt.ylabel("Accuracy (%)")
plt.title("CRAG Routing Accuracy")

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig("results/routing_accuracy.png")
plt.close()


# --------------------------------
# Print results
# --------------------------------

print("Plots saved successfully!")
print(f"Average Naive RAG latency: {naive_latency:.2f} seconds")
print(f"Average CRAG latency: {crag_latency:.2f} seconds")
print(f"CRAG routing accuracy: {routing_accuracy:.2f}%")