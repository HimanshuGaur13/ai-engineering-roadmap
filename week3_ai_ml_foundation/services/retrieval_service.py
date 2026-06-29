from services.embedding_service import (generate_embeddings)
from services.vector_store_service import (load_embeddings)
from utils.similarity_helper import (calculate_similarity)
# Function to retrieve relevant documents based on similarity scores

def retrieve_documents(query):
    document_embeddings = load_embeddings(
        "vector_store/document_embeddings.npy"  # Load stored embeddings
    )
    query_embedding = generate_embeddings([query])  # Generate embedding for the query

    similarities = calculate_similarity(
        query_embedding,
        document_embeddings
    ) # Calculate cosine similarity between query embedding and document embeddings
    print("\nDEBUG Similarities:")
    return similarities

