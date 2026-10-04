def create_chunks(text, chunk_size=500, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


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


# Experiment 1
chunks_1 = create_chunks(
    sample_text,
    chunk_size=100,
    overlap=20
)

print("===== Experiment 1 =====")
print("Chunk size: 100")
print("Overlap: 20")
print("Number of chunks:", len(chunks_1))


# Experiment 2
chunks_2 = create_chunks(
    sample_text,
    chunk_size=200,
    overlap=40
)

print("\n===== Experiment 2 =====")
print("Chunk size: 200")
print("Overlap: 40")
print("Number of chunks:", len(chunks_2))