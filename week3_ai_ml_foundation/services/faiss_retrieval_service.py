import numpy as np
from services.embedding_service import generate_embeddings
from services.vector_store_service import load_index

def retrieve_documents_faiss(query,top_k=3):
    index = load_index("vector_store/faiss_index.bin")
    query_embedding = generate_embeddings([query])
    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    return distances, indices