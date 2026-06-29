from services.embedding_service import generate_embeddings
from services.vector_store_service import create_index
from services.llm_service import ask_llm

import numpy as np


class RAGService:

    def __init__(self, chunks):

        self.chunks = chunks

        embeddings = generate_embeddings(chunks)

        self.index = create_index(embeddings)

    def retrieve_context(
        self,
        question,
        top_k=3
    ):

        query_embedding = generate_embeddings([question])

        distances, indices = self.index.search(
            np.array(query_embedding).astype("float32"),
            top_k
        )

        print("\nTop Retrieved Chunks")

        contexts = []

        for score, idx in zip(distances[0], indices[0]):

            print(f"Score: {score:.4f}")
            print(self.chunks[idx])
            print("-" * 50)

            contexts.append(self.chunks[idx])

        # IMPORTANT
        return "\n".join(contexts)

    def ask(self, question):

        context = self.retrieve_context(question)

        prompt = f"""
You are an AI HR assistant.

Use ONLY the information provided in the context.

Rules:
- Do not make up information.
- If the answer is not in the context, reply:
  "I could not find that information in the provided documents."
- Keep the answer concise.
- Mention the relevant policy if applicable.

Context:
{context}

Question:
{question}

Answer:
"""

        answer = ask_llm(prompt)

        # IMPORTANT
        return {
            "answer": answer,
            "source": context
        }