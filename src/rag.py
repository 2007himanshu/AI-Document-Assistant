from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


PDF_PATH = "data/document.pdf"


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        pages.append({
            "page": page_number,
            "text": text
        })

    return pages


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


def build_chunks(pages):
    all_chunks = []

    for page in pages:
        chunks = create_chunks(page["text"])

        for chunk in chunks:
            all_chunks.append({
                "page": page["page"],
                "text": chunk
            })

    return all_chunks


def retrieve(question, chunks, model):

    texts = [chunk["text"] for chunk in chunks]

    chunk_embeddings = model.encode(texts)

    question_embedding = model.encode([question])

    similarities = cosine_similarity(
        question_embedding,
        chunk_embeddings
    )[0]

    best_index = similarities.argmax()

    return chunks[best_index], similarities[best_index]


def generate_answer(question, passage):

    sentences = passage["text"].split(".")

    question_words = set(question.lower().split())

    best_sentence = ""
    best_score = 0

    for sentence in sentences:

        sentence_words = set(sentence.lower().split())

        score = len(question_words.intersection(sentence_words))

        if score > best_score:
            best_score = score
            best_sentence = sentence.strip()

    if best_sentence:
        return best_sentence

    return "The document does not contain enough information to answer this question."


model = SentenceTransformer("all-MiniLM-L6-v2")


# Dummy data for testing
pages = extract_text(PDF_PATH)

chunks = build_chunks(pages)

print("Pages:", len(pages))
print("Chunks:", len(chunks))

question ="Who is the current community lead?"

result, score = retrieve(question, chunks, model)

print("\nQuestion:")
print(question)

print("\nRetrieved Passage:")
print(result["text"])

print("\nSource Page:")
print(result["page"])

print("\nSimilarity Score:")
print(score)


answer = generate_answer(question, result)

print("\nAnswer:")
print(answer)