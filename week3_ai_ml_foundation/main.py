from services.search_service import semantic_search
from services.faiss_retrieval_service import retrieve_documents_faiss
from utils.file_loader import load_documents

def main():
    query = input("Enter your search query: ")
    print("\n========== COSINE SEARCH ==========\n")
    cosine_results = semantic_search(query)
    
    # for _, row in cosine_results.head(3).iterrows():
    #     print(f"Score : {row['similarity']:.4f}")
    #     print(f"Text  : {row['text']}")
    #     print("-" * 50)
    print(
    cosine_results[
        ["category", "text", "similarity"]
    ].head(5)
)

    print("\n========== FAISS SEARCH ==========\n")
    data = load_documents("datasets/documents.csv")
    distances, indices = retrieve_documents_faiss(query)
    for idx in indices[0]:
        print(data.iloc[idx]["text"])
        print("-" * 50)

if __name__ == "__main__":
    main()