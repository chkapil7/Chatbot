from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        # Load the SentenceTransformer model once
        self.model = SentenceTransformer(model_name)

    def embed(self, texts):
        """
        Generate embeddings for a list of texts.
        :param texts: List[str] or single string
        :return: numpy.ndarray of embeddings
        """
        if isinstance(texts, str):
            texts = [texts]
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings

# FAISS helper functions

def load_faiss_index(index_path):
    """
    Load a FAISS index from a file.
    """
    index = faiss.read_index(index_path)
    return index

def search_faiss_index(index, query_embedding, top_k=5):
    """
    Search the FAISS index for the nearest neighbors to query_embedding.
    """
    if query_embedding.ndim == 1:
        query_embedding = query_embedding[np.newaxis, :]
    distances, indices = index.search(query_embedding, top_k)
    return distances, indices

# Example usage for testing
if __name__ == "__main__":
    embedder = Embedder()
    sample_texts = [
        "This is a test sentence.",
        "FAISS helps with similarity search."
    ]
    embeddings = embedder.embed(sample_texts)
    print("Embeddings shape:", embeddings.shape)

    # Example: create a FAISS index and save it (for demonstration)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, "test.index")

    # Load the index and search
    loaded_index = load_faiss_index("test.index")
    dists, inds = search_faiss_index(loaded_index, embeddings[0], top_k=2)
    print("Distances:", dists)
    print("Indices:", inds)
