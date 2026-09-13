from google import genai
from pydantic import BaseModel, Field

from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)

GRADING_MODEL = "gemini-3.5-flash-lite"


class RelevanceGrade(BaseModel):
    relevant: bool = Field(
        description="Whether the document contains information that directly helps answer the question."
    )


def grade_document(query: str, document: str) -> bool:
    prompt = f"""
You are a strict document relevance grader.

Determine whether the document contains information that directly helps answer
the user's question.

Return relevant=true ONLY when the document provides useful information for
answering the question.

Return relevant=false when the document is unrelated or does not provide
useful information.

User question:
{query}

Document:
{document}
"""

    response = client.models.generate_content(
        model=GRADING_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": RelevanceGrade,
        },
    )

    result = RelevanceGrade.model_validate_json(response.text)

    return result.relevant