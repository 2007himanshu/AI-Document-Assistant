# Decisions and Experiments

## 1. Project Approach

We built a document question-answering system using a Retrieval-Augmented
Generation (RAG) style pipeline.

The pipeline consists of:

PDF → Text Extraction → Chunking → Embeddings → Retrieval → Answer

## 2. Chunking Experiment

### Initial Setting

- Chunk size: 500 characters
- Overlap: 50 characters

This setting was selected to keep chunks small enough for retrieval while
maintaining some context between neighboring chunks.

### Alternative Setting

We will compare this with:

- Chunk size: 1000 characters
- Overlap: 100 characters

The difference will be evaluated using the test questions.

## 3. Retrieval Approach

We used sentence-transformer embeddings with the
`all-MiniLM-L6-v2` model.

Cosine similarity is used to compare the question embedding with document
chunk embeddings.

## 4. Failed / Limited Approach

During development, we initially tested the chunking and retrieval pipeline
using manually created sample text because the original GDG-USAR document
was not available in the task message.

This was useful for testing the pipeline, but it is not representative of
the final document. The final evaluation will therefore be performed using
the actual project document.

## 5. Important Change

The system was designed to return the retrieved passage and its source page
along with the answer. This was done to make the answers traceable to the
document.

## 6. Limitation

The current prototype uses a simple retrieval-based answer method.
Therefore, answer quality depends strongly on retrieving a relevant chunk.

## 7. Chunking Comparison Experiment

We compared two chunking configurations using the same sample document and
the same question.

### Experiment 1

- Chunk size: 100 characters
- Overlap: 20 characters

### Experiment 2

- Chunk size: 200 characters
- Overlap: 40 characters

### Observation

Smaller chunks produced more individual chunks and focused more closely on
specific pieces of information.

Larger chunks produced fewer chunks and preserved more surrounding context.

The final configuration will be selected after testing both settings on the
actual GDG-USAR document.

## Chunking and Retrieval Experiment

### Experiment 1
- Chunk size: 100 characters
- Overlap: 20 characters

### Experiment 2
- Chunk size: 200 characters
- Overlap: 40 characters

### Observation
Smaller chunks can provide more focused passages, but may split related information across multiple chunks.

Larger chunks preserve more surrounding context, but may retrieve extra information that is not directly relevant to the question.

For the prototype, both configurations were tested to compare retrieval behavior. The final configuration can be selected based on which setting provides more relevant context for the source document.

### Retrieval Method
- Embedding model: all-MiniLM-L6-v2
- Similarity method: Cosine similarity
- Retrieved result: Highest similarity passage
- Source tracking: Page number is preserved with each chunk