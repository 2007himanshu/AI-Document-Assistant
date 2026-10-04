from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Artificial Intelligence is a field of computer science.",
    "Machine learning allows computers to learn from data.",
    "I like eating pizza."
]

embeddings = model.encode(texts)

print("Number of texts:", len(texts))
print("Embedding shape:", embeddings.shape)