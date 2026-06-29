from utils.file_loader import load_documents
from utils.text_preprocessor import preprocess_text
from services.embedding_service import (generate_embeddings)
from services.vector_store_service import (save_embeddings,create_index,save_index)

# This file should be run ONCE. It generates the embeddings for the documents and saves them to disk.
# It also creates a FAISS index from the embeddings and saves it to disk. 

data = load_documents("datasets/documents.csv")                  # Load dataset
documents = data["text"].tolist()                                # Extract documents from the dataset
processed_documents = [preprocess_text(doc)for doc in documents] # Preprocess documents for better embedding generation
embeddings = generate_embeddings(processed_documents )           # Generate embeddings for the preprocessed documents
save_embeddings(embeddings,"vector_store/document_embeddings.npy")# Save the generated embeddings to disk
index = create_index(embeddings)                                 # Create a FAISS index from the generated embeddings
save_index(index,"vector_store/faiss_index.bin")                 # Save the FAISS index to disk
print("FAISS index created successfully.")   