# AskMyPDF – AI Document Assistant

AskMyPDF is a beginner-friendly **Retrieval-Augmented Generation (RAG)** application. Upload a PDF, ask a question, retrieve relevant text passages using embedding similarity, and generate an answer grounded in those passages.

## Features

- Upload and read PDF documents
- Extract text page by page
- Split text into overlapping chunks
- Create embeddings with `text-embedding-3-small`
- Retrieve relevant passages using cosine similarity
- Generate grounded answers with `gpt-4o-mini`
- Display retrieved excerpts and page numbers
- Basic unit tests for chunking and retrieval

## Architecture

1. **Ingestion:** `pypdf` extracts text from each PDF page.
2. **Chunking:** `rag_utils.py` splits page text into overlapping chunks.
3. **Embedding:** OpenAI converts each chunk into a numerical vector.
4. **Retrieval:** Cosine similarity ranks chunks against the question embedding.
5. **Generation:** The LLM answers using the retrieved passages and cites page numbers.

```text
PDF Upload
   |
   v
Text Extraction (PyPDF)
   |
   v
Chunking with Overlap
   |
   v
Embeddings (OpenAI)
   |
   v
Similarity Search (NumPy)
   |
   v
Relevant Context + User Question
   |
   v
LLM Answer (GPT-4o-mini)
```

## Requirements

- Python 3.10 or newer
- An OpenAI API key with API access and available billing/credits
- Internet connection for API calls

## Run locally

```bash
# 1. Clone your repository
git clone https://github.com/imadabathinisowjanya/askmypdf.git
cd askmypdf

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the application
streamlit run app.py
```

Open the local URL printed by Streamlit, enter your API key in the sidebar, upload a text-based PDF, and click **Process PDF**.

## Run tests

```bash
pytest -q
```

## Project structure

```text
askmypdf/
├── app.py
├── rag_utils.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── tests/
    └── test_rag_utils.py
```

## Important notes

- This project sends document excerpts and questions to the OpenAI API. Do not upload confidential, personal, or sensitive documents.
- API usage may incur charges. Check current pricing before use.
- Scanned/image-only PDFs may not contain extractable text; OCR is not included.
- This is a learning project, not a production-ready system. It does not include authentication, persistent vector storage, rate limiting, or production monitoring.
- Never paste your API key into source code or commit it to GitHub.

## Skills demonstrated

Python · Generative AI · Large Language Models · RAG · Embeddings · Semantic Search · Prompt Engineering · Streamlit · REST API usage · Unit Testing
