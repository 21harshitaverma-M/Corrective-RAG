from generator import generate_answer


query = "What is supervised learning?"

context = """
Supervised learning is a type of machine learning that uses labeled
training data to learn a relationship between inputs and known outputs.
It can be used for tasks such as classification and regression.
"""


answer = generate_answer(
    query,
    context
)

print("\nANSWER:")
print(answer)