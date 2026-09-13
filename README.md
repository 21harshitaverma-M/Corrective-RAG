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

## Experimental Results

The system was evaluated by comparing Naive RAG with Corrective RAG on the same set of test queries.

### Results

| Metric | Naive RAG | Corrective RAG |
|---|---:|---:|
| Average Latency | 6.95 s | 11.61 s |
| Routing Accuracy | — | 100.00% |

### Observations

- Naive RAG had lower average latency at 6.95 seconds.
- Corrective RAG had higher average latency at 11.61 seconds because it performs an additional document relevance-grading step.
- Corrective RAG achieved 100% routing accuracy on the evaluated test queries.
- The experiment therefore shows a trade-off between additional processing time and improved retrieval-source routing for the tested queries.

> These results are specific to the experimental dataset and test queries used in this project and should not be interpreted as universal performance guarantees.

## Research Conclusion

The experiment indicates that evaluating retrieved documents before generation can improve routing reliability in the tested CRAG system. However, this additional evaluation introduces latency compared with standard Naive RAG.

Therefore, for the tested queries, Corrective RAG provides more controlled retrieval routing at the cost of additional processing time.

## Limitations

- The evaluation uses a small curated knowledge base.
- The number of test queries is limited.
- Latency depends on API response times and network conditions.
- The experiment does not establish that CRAG is universally more accurate than Naive RAG.
- Web-search results can change over time.

## Future Work

Future improvements could include:

- Larger and more diverse evaluation datasets.
- Query rewriting before retrieval.
- Sentence-level relevance filtering.
- Confidence-based routing.
- Evaluation with larger vector databases such as Qdrant or pgvector.
- More systematic evaluation of hallucination and factual support.
- Deployment as a containerized API service.