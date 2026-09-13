from grader import grade_document


query = "What is supervised learning?"

relevant_document = """
Machine learning is a branch of artificial intelligence that enables
computers to learn patterns from data and make predictions or decisions.
Supervised learning uses labeled data to learn a mapping between inputs
and known outputs.
"""

irrelevant_document = """
A database is an organized collection of data. Relational databases
store data in tables consisting of rows and columns. SQL can be used
to query and manage relational databases.
"""


print("Relevant document:")
print(grade_document(query, relevant_document))

print("\nIrrelevant document:")
print(grade_document(query, irrelevant_document))