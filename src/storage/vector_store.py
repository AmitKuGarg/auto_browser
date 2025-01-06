import json
import os
from typing import List, Dict

import faiss
import numpy as np

from src.embeddings.openai_embeddings import OpenAIEmbeddings


class VectorStore:
    def __init__(self, embedding_dim: int = 3072):  # text-embedding-3-large dimension
        self.embeddings = OpenAIEmbeddings()
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents: List[Dict] = []

    def search(self, query: str, k: int = 5) -> List[Dict]:
        """Search for similar documents using the query."""
        # Create query embedding
        query_embedding = self.embeddings.create_embedding(query)

        # Search in FAISS index
        distances, indices = self.index.search(
            np.array([query_embedding], dtype=np.float32),
            k
        )

        # Return matched documents
        results = []
        for idx, distance in zip(indices[0], distances[0]):
            if idx != -1:  # Valid index
                doc = self.documents[idx]
                results.append({
                    'url': doc['url'],
                    'content': doc['content']
                })

        return results

    def load(self, directory: str):
        """Load vector store from disk."""
        # Load FAISS index
        self.index = faiss.read_index(os.path.join(directory, 'index.faiss'))

        # Load documents
        with open(os.path.join(directory, 'documents.json'), 'r') as f:
            self.documents = json.load(f)
