import os
import time
import chromadb
from chromadb.utils import embedding_functions
from google import genai

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found!")
    exit()

# Gemini client
client = genai.Client(api_key=api_key)

# ChromaDB
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_collection(
    name="dsa_documents",
    embedding_function=embedding_function
)

question = "What are the operations performed on a queue?"


def generate_answer(prompt):
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            print(f"Gemini attempt {attempt + 1} failed.")
            print("Error:", e)

            if attempt < 2:
                print("Retrying in 5 seconds...\n")
                time.sleep(5)

    return "Gemini is temporarily unavailable. Please try again later."


# -----------------------------
# WITHOUT RAG
# -----------------------------

no_rag_prompt = f"""
Answer this question using your general knowledge.

Question:
{question}

Give a clear beginner-friendly answer.
"""

print("Generating WITHOUT RAG answer...")
no_rag_answer = generate_answer(no_rag_prompt)


# -----------------------------
# RETRIEVE DOCUMENT
# -----------------------------

results = collection.query(
    query_texts=[question],
    n_results=3
)

context = "\n\n".join(results["documents"][0])


# -----------------------------
# WITH RAG
# -----------------------------

rag_prompt = f"""
Answer the question using ONLY the document context below.

If the answer is not available in the context, say:
"The information is not available in the document."

Document context:
{context}

Question:
{question}

Give a clear beginner-friendly answer.
"""

print("Generating WITH RAG answer...")
rag_answer = generate_answer(rag_prompt)


# -----------------------------
# DISPLAY RESULTS
# -----------------------------

print("\n" + "=" * 60)
print("RAG vs NO-RAG COMPARISON")
print("=" * 60)

print("\nQuestion:")
print(question)

print("\n" + "-" * 60)
print("WITHOUT RAG")
print("-" * 60)
print(no_rag_answer)

print("\n" + "-" * 60)
print("WITH RAG")
print("-" * 60)
print(rag_answer)

print("\n" + "=" * 60)