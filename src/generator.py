from google import genai

from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)

GENERATION_MODEL = "gemini-3.5-flash-lite"


def generate_answer(query: str, context: str) -> str:

    prompt = f"""
You are a grounded question-answering system.

Answer the user's question using ONLY the provided context.

Do not use outside knowledge.

If the context does not contain enough information to answer the
question, clearly say that the available context is insufficient.

User question:
{query}

Context:
{context}

Answer:
"""

    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt
    )

    return response.text