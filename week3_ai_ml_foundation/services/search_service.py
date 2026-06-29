from utils.file_loader import (load_documents)
from services.retrieval_service import (retrieve_documents)

def semantic_search(query):
    data = load_documents("datasets/documents.csv")           
    similarities = retrieve_documents(query)             # Retrieve similarity scores for the query against all documents     
    data["similarity"] = similarities[0]  
    return data.sort_values(
        by="similarity",
        ascending=False
    )