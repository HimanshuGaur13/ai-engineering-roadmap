main.py
 │
 │ query = "chatgpt"
 ▼

search_service.py
 │
 │ load csv
 ▼

retrieval_service.py
 │
 │ load embeddings
 │ generate query embedding
 ▼

embedding_service.py
 │
 │ text → vector
 ▼

similarity_helper.py
 │
 │ cosine similarity
 ▼

search_service.py
 │
 │ attach scores
 │ sort descending
 ▼

main.py
 │
 ▼

Top Results