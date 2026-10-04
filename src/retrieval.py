from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


sample_text = """
Artificial Intelligence is a field of computer science.
Machine learning allows computers to learn from data.
Deep learning uses neural networks to solve complex problems.
Natural language processing helps computers understand human language.
Machine learning is used in recommendation systems, image recognition,
speech recognition, and fraud detection.
Artificial intelligence is also used in healthcare, transportation,
education, and many other fields.
"""


def create_chunks(text, chunk_size, overlap):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def retrieve(question, chunks):
    chunk_embeddings = model.encode(chunks)
    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        chunk_embeddings
    )[0]

    best_index = similarities.argmax()

    return chunks[best_index], similarities[best_index]


question = "What is machine learning?"


# Experiment 1
chunks_1 = create_chunks(
    sample_text,
    chunk_size=100,
    overlap=20
)

result_1, score_1 = retrieve(question, chunks_1)

print("===== Experiment 1 =====")
print("Retrieved passage:")
print(result_1)
print("Similarity:", round(float(score_1), 4))


# Experiment 2
chunks_2 = create_chunks(
    sample_text,
    chunk_size=200,
    overlap=40
)

result_2, score_2 = retrieve(question, chunks_2)

print("\n===== Experiment 2 =====")
print("Retrieved passage:")
print(result_2)
print("Similarity:", round(float(score_2), 4))