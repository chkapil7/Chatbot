import faiss
import pickle
from sentence_transformers import SentenceTransformer

# 🔹 1. Load your documents
# You can customize this part based on your data source
with open("docs.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f if line.strip()]

# 🔹 2. Create embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(documents, convert_to_numpy=True)

# 🔹 3. Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 🔹 4. Save documents and FAISS index
with open("documents.pkl", "wb") as f:
    pickle.dump(documents, f)

faiss.write_index(index, "faiss.index")

print("✅ Saved: documents.pkl and faiss.index")
#         raise HTTPException(status_code=400, detail="Query cannot be empty")
#   # Retrieve relevant documents                   