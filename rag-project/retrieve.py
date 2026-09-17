
import chromadb
from chromadb.utils import embedding_functions

# Load the same embedding model used during storage
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Get the existing collection
collection = client.get_collection(
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

print("Question:", question)
print("\nRelevant chunks:\n")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"--- Result {i} ---")
    print(document[:500])
    print()