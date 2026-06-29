# from sentence_transformers import SentenceTransformer

# from sklearn.metrics.pairwise import (
#     cosine_similarity
# )

# # Load model
# model = SentenceTransformer(
#     'all-MiniLM-L6-v2'
# )

# # Sentences
# sentences = [
#     "I love AI",
#     "Artificial Intelligence is amazing"
# ]

# # Generate embeddings
# embeddings = model.encode(sentences)

# # Compare embeddings
# similarity = cosine_similarity(
#     [embeddings[0]],
#     [embeddings[1]]
# )

# # Print similarity
# print("Cosine Similarity:")
# print(similarity)