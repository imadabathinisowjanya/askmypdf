# 📄 AskMyPDF – AI Document Assistant

An AI-powered PDF chatbot built using Python, Streamlit, Ollama, and Retrieval-Augmented Generation (RAG).

AskMyPDF allows users to upload PDF documents and ask questions about their contents. It retrieves relevant document sections and generates answers using locally running AI models.

## 🚀 Features

* Upload and process PDF documents.
* Extract text from PDF files.
* Split text into overlapping chunks.
* Generate local text embeddings using Ollama.
* Retrieve relevant document sections using cosine similarity.
* Generate answers using Llama 3.2.
* Display retrieved document excerpts.
* Cite page numbers in answers.
* Run locally without paid OpenAI API credits.

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* Llama 3.2
* Nomic Embed Text
* NumPy
* PyPDF
* Retrieval-Augmented Generation (RAG)
* Pytest

## 📁 Project Structure

```text
askmypdf/
│
├── app.py
├── rag\_utils.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
└── tests/
    └── test\_rag\_utils.py
```

## ⚙️ Installation and Setup

### 1\. Clone the repository

```bash
git clone https://github.com/imadabathinisowjanya/askmypdf.git
cd askmypdf
```

### 2\. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 3\. Install Ollama

Download and install Ollama:

https://ollama.com/download

### 4\. Download AI models

Open a terminal and run:

```bash
ollama pull nomic-embed-text
ollama pull llama3.2
```

### 5\. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

`http://localhost:8501`

## 💡 How It Works

1. Upload a PDF document.
2. Extract text from the PDF.
3. Divide the extracted text into overlapping chunks.
4. Generate embeddings using the Nomic embedding model.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant document chunks using cosine similarity.
7. Pass the retrieved context to Llama 3.2.
8. Generate an answer based on the uploaded document.

## 🧪 Run Tests

Execute the following command:

```bash
python -m pytest -q
```

## 🔮 Future Enhancements

* Support multiple PDF documents.
* Add conversation history.
* Improve source citations.
* Support scanned PDFs using OCR.
* Add document summarization.
* Improve retrieval accuracy.

## 👩‍💻 Author

**Sowjanya Imadabathini**

GitHub: https://github.com/imadabathinisowjanya

LinkedIn: https://www.linkedin.com/in/sowjanyaimadabathini5/

\---

Built as a hands-on project to explore Generative AI, Large Language Models, and Retrieval-Augmented Generation using locally running AI models.

\---



\## Application Screenshots



\### Application Interface

!\[AskMyPDF Interface](screenshots/app-interface.png)



\### AI Question and Answer

!\[AskMyPDF Answer](screenshots/question-answer1.png)



\### Retrieved Document Excerpts

!\[Retrieved Excerpts](screenshots/question-answer2.png)



\---



\## RAG Architecture



```mermaid

flowchart TD

&#x20;   A\[User uploads PDF] --> B\[PDF Text Extraction]

&#x20;   B --> C\[Text Chunking with Overlap]

&#x20;   C --> D\[Ollama Embedding Model]

&#x20;   D --> E\[Document Vectors]



&#x20;   F\[User enters a question] --> G\[Question Embedding]

&#x20;   G --> H\[Cosine Similarity Search]

&#x20;   E --> H



&#x20;   H --> I\[Top 4 Relevant Chunks]

&#x20;   I --> J\[Context with Page Numbers]

&#x20;   J --> K\[Ollama Llama 3.2]

&#x20;   K --> L\[Generated Answer]

&#x20;   L --> M\[Streamlit Interface]

```



\## Technology Stack



| Component | Technology |

|---|---|

| Programming Language | Python |

| User Interface | Streamlit |

| PDF Processing | PyPDF |

| Embeddings | Ollama – nomic-embed-text |

| Language Model | Ollama – Llama 3.2 |

| Similarity Search | NumPy |

| Testing | Pytest |

| Architecture | Retrieval-Augmented Generation |



