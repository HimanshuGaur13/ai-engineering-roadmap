from sentence_transformers import SentenceTransformer 
# Load the pre-trained model Converts text into vectors.
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def generate_embeddings(texts):

    return model.encode(texts) # Generate embeddings for the input texts