import os
import chromadb
from chromadb.utils import embedding_functions
from google import genai

# Check API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Gemini API key not found!")
    exit()

# Connect to Gemini
client = genai.Client(api_key=api_key)

# Use the same embedding function used while storing chunks
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_collection(
    name="dsa_documents",
    embedding_function=embedding_function
)

# User question
question = "What are the operations performed on a queue?"

# Retrieve relevant chunks
results = collection.query(
    query_texts=[question],
    n_results=3
)

# Combine retrieved documents
context = "\n\n".join(results["documents"][0])

# Create grounded prompt
prompt = f"""
You are a helpful assistant answering questions using the provided document context.

Rules:
1. Answer only using the context.
2. If the answer is not available in the context, say:
   "The information is not available in the document."
3. Give a clear and beginner-friendly answer.

Document context:
{context}

Question:
{question}

Answer:
"""

# Generate answer using Gemini
response = client.models.generate_content(
  model="gemini-3.6-flash",
    contents=prompt
)

print("\nQuestion:")
print(question)

print("\nGenerated Answer:")
print(response.text)