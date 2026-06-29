import os

from services.rag_service import (
    RAGService
)

from utils.document_loader import (
    load_text_document
)

from utils.chunker import (
    chunk_text
)

# Load all documents
all_text = ""

documents_folder = "documents"

for file in os.listdir(documents_folder):

    if file.endswith(".txt"):

        file_path = os.path.join(
            documents_folder,
            file
        )

        print(f"Loaded: {file}")

        all_text += (
            load_text_document(file_path)
            + "\n\n"
        )

# Create chunks
chunks = chunk_text(all_text)

# Initialize RAG
rag = RAGService(chunks)

print("\nAI Knowledge Assistant Ready!")
print("Type 'exit' to quit.")

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    result = rag.ask(question)

    print("\n==============================")
    print("Answer")
    print("==============================")
    print(result["answer"])

    print("\n==============================")
    print("Retrieved Context")
    print("==============================")
    print(result["source"])