# Corrective RAG: A Self-Evaluating Retrieval-Augmented Generation System

## Research Question

Does evaluating retrieved documents before generation improve the reliability of a Retrieval-Augmented Generation (RAG) system compared with standard Naive RAG?

## Overview

This project implements and evaluates a Corrective Retrieval-Augmented Generation (CRAG) pipeline.

Unlike Naive RAG, which directly sends retrieved documents to the language model, CRAG evaluates whether the retrieved documents are relevant to the user's query before generating an answer.

If relevant local knowledge is found, the system uses it as context.

If the retrieved documents are not relevant, the system automatically performs a web search and uses the retrieved web information as context.

## System Architecture

### Naive RAG

Query → Embedding → FAISS Retrieval → Top-K Documents → LLM → Answer

### Corrective RAG

Query
↓
Embedding
↓
FAISS Retrieval
↓
Document Relevance Grading
↓
Relevant?
├── Yes → Local Knowledge → LLM
└── No → Web Search → LLM
↓
Answer

## Technologies Used

- Python
- FAISS
- OpenAI Embeddings
- Google Gemini
- Tavily Web Search
- Pydantic
- FastAPI
- Docker
- GitHub Actions

## Knowledge Base

The local knowledge base contains curated documents covering:

- Machine Learning
- Natural Language Processing
- Deep Learning
- Computer Vision
- Databases

## Experimental Evaluation

Six questions were evaluated using both Naive RAG and Corrective RAG.

The experiment included:

1. Questions answerable from the local knowledge base
2. Questions requiring fresh external information
3. Comparison of Naive RAG and CRAG answers
4. Document relevance grading
5. Routing accuracy
6. Latency measurement
7. Keyword-based answer coverage

## Observed Results

The implemented experiment achieved:

- **CRAG routing accuracy:** 100%
- **Average Naive RAG latency:** 6.95 seconds
- **Average CRAG latency:** 11.61 seconds

CRAG correctly routed all six experimental questions to either the local knowledge base or web fallback.

The results also show a trade-off: CRAG introduced additional latency because it performs document evaluation before deciding whether web retrieval is necessary.

## Example

For:

> What is supervised learning?

CRAG identified `machine_learning.txt` as relevant and used the local knowledge base.

For:

> What is Nvidia's current market capitalization?

The local documents were judged irrelevant, so CRAG triggered web fallback.

## Project Structure

```text
Corrective-RAG/
│
├── data/
│   └── knowledge_base/
│       ├── machine_learning.txt
│       ├── natural_language_processing.txt
│       ├── deep_learning.txt
│       ├── computer_vision.txt
│       └── databases.txt
│
├── src/
│   ├── embeddings.py
│   ├── retriever.py
│   ├── grader.py
│   ├── generator.py
│   ├── web_search.py
│   ├── naive_rag.py
│   ├── crag.py
│   ├── experiment.py
│   ├── analyze_results.py
│   └── evaluate_answers.py
│
├── results/
├── tests/
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
Docker

The project can be built and executed using Docker.

docker build -t corrective-rag .
docker run --rm --env-file .env corrective-rag

API keys are supplied through environment variables and are not included in the repository.

Conclusion

The experiment demonstrates that adding a relevance-evaluation and routing stage can enable a RAG system to distinguish between locally answerable questions and questions requiring external retrieval.

However, the additional grading step increases latency. Therefore, CRAG provides a reliability-oriented routing mechanism at the cost of additional computation and response time.

Future Improvements
Larger evaluation dataset
More robust answer-quality metrics
Query rewriting
Sentence-level context filtering
Confidence-based routing
Vector databases such as Qdrant or pgvector
More extensive latency and cost analysis

### ⚠️ One important thing

Those **6.95 s / 11.61 s / 100%** numbers are YOUR actual experiment results from the run you just showed me, so we're good to document them.

Also, don't worry about the Google Gemini warning:

```text
Direct use of automatic function calling (AFC)...