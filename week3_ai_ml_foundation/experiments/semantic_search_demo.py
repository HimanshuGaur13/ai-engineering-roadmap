# import pandas as pd

# from sentence_transformers import (
#     SentenceTransformer
# )

# from sklearn.metrics.pairwise import (
#     cosine_similarity
# )

# # Load model
# model = SentenceTransformer(
#     'all-MiniLM-L6-v2'
# )

# # Load dataset
# data = pd.read_csv(
#     "datasets/documents.csv"
# )

# # Convert dataset to list
# documents = data["text"].tolist()

# # Generate embeddings for documents
# doc_embeddings = model.encode(
#     documents
# )

# # User query
# query = "Artificial Intelligence"

# # Generate query embedding
# query_embedding = model.encode(
#     [query]
# )

# # Compare query with documents
# similarities = cosine_similarity(
#     query_embedding,
#     doc_embeddings
# )

# # Add similarity score to dataframe
# data["similarity"] = similarities[0]

# # Sort by similarity
# results = data.sort_values(
#     by="similarity",
#     ascending=False
# )

# # Print ranked results
# print(results[["text", "similarity"]])