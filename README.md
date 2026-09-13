# Corrective RAG: A Self-Evaluating Retrieval-Augmented Generation System

## Research Question

Does evaluating retrieved documents before generation improve the reliability
of a Retrieval-Augmented Generation system compared with standard Naive RAG?

## Overview

This project implements and evaluates a Corrective Retrieval-Augmented
Generation (CRAG) pipeline.

Unlike standard Naive RAG, which directly passes retrieved documents to an
LLM, the proposed system evaluates retrieved documents for relevance before
generation.

If relevant local documents are found, they are used as context.

If no retrieved document is relevant, the system performs a web search using
Tavily and uses the retrieved web evidence for answer generation.

## System Architecture

### Naive RAG

Query
→ Embedding
→ FAISS Retrieval
→ Top-K Documents
→ Gemini
→ Answer

### Corrective RAG

Query
→ Embedding
→ FAISS Retrieval
→ Document Grader
→ Relevant?
→ Local Context / Web Fallback
→ Gemini
→ Answer

## Technologies Used

- Python
- Google Gemini API
- Gemini Embeddings
- FAISS
- Pydantic
- Tavily
- FastAPI
- Docker
- GitHub Actions

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
├── results/
│   └── experiment_results.csv
│
├── src/
│   ├── config.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── grader.py
│   ├── web_search.py
│   ├── generator.py
│   ├── crag.py
│   ├── naive_rag.py
│   ├── experiment.py
│   ├── analyze_results.py
│   └── evaluate_answers.py
│
├── tests/
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md