
from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np

# 1. Load the embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 2. Sample texts to create embeddings for
texts = [
    "The cat sits on the mat",
    "A feline rests on a rug",
    "I love programming",
    "Python is a great language"
]

# 3. Create embeddings
vectors = embeddings.embed_documents(texts)

# 4. Show results
print("=== Text Embeddings Demo ===\n")

for i, (text, vector) in enumerate(zip(texts, vectors)):
    print(f"Text {i+1}: {text}")
    print(f"Embedding shape: {len(vector)} dimensions")
    print(f"First 5 values: {vector[:5]}")
    print()

# 5. Calculate similarity between first two texts
similarity = np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))
print(f"Cosine similarity between '{texts[0]}' and '{texts[1]}': {similarity:.4f}")

# 6. Calculate similarity between unrelated texts
similarity_unrelated = np.dot(vectors[0], vectors[2]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[2]))
print(f"Cosine similarity between '{texts[0]}' and '{texts[2]}': {similarity_unrelated:.4f}")