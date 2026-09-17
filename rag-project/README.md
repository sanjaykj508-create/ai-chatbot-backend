\# Retrieval-Augmented Generation (RAG) System



\## Project Overview



This project implements a Retrieval-Augmented Generation (RAG) system that allows an LLM to answer questions using information retrieved from a user-provided document.



For this project, `Unit-II DSA.pdf` is used as the source document. The document is converted into text, divided into smaller chunks, stored in ChromaDB, and retrieved when a user asks a question.



The retrieved information is then provided to the Gemini LLM to generate a grounded answer.



\## Technologies Used



\* Python

\* Google Gemini API

\* ChromaDB

\* Sentence Transformers

\* PyPDF

\* PowerShell

\* Virtual Environment (venv)



\## RAG Architecture



```text

PDF Document

&#x20;    ↓

Extract Text

&#x20;    ↓

Chunk the Text

&#x20;    ↓

Generate Embeddings

&#x20;    ↓

Store in ChromaDB

&#x20;    ↓

User Question

&#x20;    ↓

Similarity Search

&#x20;    ↓

Retrieve Relevant Chunks

&#x20;    ↓

Send Context + Question to Gemini

&#x20;    ↓

Generate Grounded Answer

```



## Project Files

| File | Purpose |
|---|---|
| `Unit-II DSA.pdf` | Source document |
| `dsa_text.txt` | Extracted text from the PDF |
| `load_pdf.py` | Extracts text from the PDF |
| `chunk_text.py` | Splits the document into chunks |
| `store_chunks.py` | Stores chunks and embeddings in ChromaDB |
| `retrieve.py` | Retrieves relevant document chunks |
| `generate.py` | Generates an answer using retrieved context and Gemini |
| `compare.py` | Compares No-RAG and RAG responses |
| `chroma_db/` | Persistent ChromaDB storage |

\## How the System Works



\### 1. Document Ingestion



The PDF document is first processed and its text is extracted.



\### 2. Chunking



The extracted text is divided into smaller overlapping chunks so that relevant sections can be retrieved efficiently.



\### 3. Embeddings



Each chunk is converted into a numerical representation called an embedding using the Sentence Transformer model:



`all-MiniLM-L6-v2`



\### 4. Vector Database



The embeddings and corresponding text chunks are stored in ChromaDB.



\### 5. Retrieval



When a question is asked, ChromaDB searches for the most relevant document chunks using similarity search.



\### 6. Generation



The retrieved chunks are added to the prompt and sent to the Gemini model.



The model generates an answer based on the retrieved document context.



\## RAG vs No-RAG



\### Question



\*\*What are the operations performed on a queue?\*\*



\### Without RAG



Without RAG, Gemini answers using its general model knowledge. The response may include explanations, examples, and information that are not necessarily taken from the specific source document.



\### With RAG



With RAG, the system retrieves relevant information from `Unit-II DSA.pdf` before generating the answer.



The retrieved document information identified the queue operations as:



\* Enqueue

\* Dequeue

\* Peek or Front

\* Rear

\* isFull

\* isEmpty



This demonstrates how RAG connects an LLM with information from a specific external document.



\## Example Output



```text

Question:

What are the operations performed on a queue?



WITHOUT RAG:

General explanation of queue operations using the model's

general knowledge.



WITH RAG:

Based on the provided document, the basic operations performed

on a queue are:



Enqueue

Dequeue

Peek or Front

Rear

isFull

isEmpty

```



\## Benefits of RAG



\* Allows an LLM to use external documents.

\* Helps answer questions using specific document content.

\* Reduces dependence on the model's general knowledge.

\* Makes it possible to build document-based question-answering systems.

\* Useful for company documents, study materials, manuals, and knowledge bases.



\## How to Run



\### 1. Activate the virtual environment



```powershell

venv\\Scripts\\Activate.ps1

```



\### 2. Extract PDF text



```powershell

python load\_pdf.py

```



\### 3. Store document chunks



```powershell

python store\_chunks.py

```



\### 4. Test retrieval



```powershell

python retrieve.py

```



\### 5. Generate a RAG answer



```powershell

python generate.py

```



\### 6. Compare RAG and No-RAG



```powershell

python compare.py

```



\## API Key Security



The Gemini API key is stored in the environment variable:



```text

GEMINI\_API\_KEY

```



API keys should never be committed to GitHub or included directly in source code.



\## Conclusion



This project demonstrates the complete RAG pipeline:



\*\*Document → Chunking → Embeddings → ChromaDB → Retrieval → Gemini → Grounded Answer\*\*



The system enables an LLM to answer questions using information retrieved from a specific document rather than relying only on its general knowledge.



