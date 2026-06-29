from sklearn.metrics.pairwise import cosine_similarity

# Function to calculate cosine similarity between query and document embeddings
# It takes the query embedding and the document embeddings as input and returns the cosine similarity scores.
def calculate_similarity(
    query_embedding,
    document_embeddings
):

    return cosine_similarity(
        query_embedding,
        document_embeddings
    )