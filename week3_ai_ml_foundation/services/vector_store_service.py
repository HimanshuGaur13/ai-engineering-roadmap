import faiss
import numpy as np

# It provides functions to save and load embeddings and FAISS indexes. 
# The embeddings are saved as .npy files, while the FAISS index is saved as a binary file.
# This allows for efficient retrieval of document embeddings during search operations.
def create_index(embeddings):
    dimension = embeddings.shape[1]                   # Get the dimensionality of the embeddings
    index = faiss.IndexFlatL2(dimension)              # Create a FAISS index for L2 distance
    index.add(np.array(embeddings).astype("float32")) # Add embeddings to the index
    return index

def save_index(index,path):
    faiss.write_index(index,path)                     # Save the FAISS index to disk

def load_index(path):
    return faiss.read_index(path)                     # Load the FAISS index from disk

def save_embeddings(embeddings, path):
    np.save(path, embeddings)

def load_embeddings(path):
    return np.load(path)