import chromadb
from pathlib import Path
from chromadb.utils import embedding_functions

# Read extracted PDF text
text = Path("dsa_text.txt").read_text(encoding="utf-8")

# Create chunks
chunk_size = 500
overlap = 100

chunks = []
start = 0

while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    start = end - overlap

# Local embedding model
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Create ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="dsa_documents",
    embedding_function=embedding_function
)

# Store chunks
for i, chunk in enumerate(chunks):
    collection.upsert(
        ids=[f"chunk_{i}"],
        documents=[chunk]
    )

print("Chunks stored successfully!")
print("Total chunks:", len(chunks))