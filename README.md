# AI-Powered Document Assistant

## Overview

This project is a document question-answering system that retrieves relevant
information from a document and uses the retrieved context to answer user
questions.

The system follows a Retrieval-Augmented Generation (RAG-style) pipeline.

## Pipeline

PDF
↓
Text Extraction
↓
Text Chunking
↓
Embeddings
↓
Similarity Retrieval
↓
Relevant Passage
↓
Answer
↓
Source Page

## Technologies Used

- Python
- PyPDF
- Sentence Transformers
- Scikit-learn
- NumPy

## How It Works

### 1. Text Extraction

The PDF document is processed using PyPDF to extract text from individual
pages.

### 2. Chunking

The extracted text is divided into smaller chunks.

The initial configuration uses:

- Chunk size: 500 characters
- Overlap: 50 characters

### 3. Embeddings

Each text chunk is converted into a numerical vector using the
`all-MiniLM-L6-v2` sentence-transformer model.

### 4. Retrieval

When a user asks a question, the question is converted into an embedding.
Cosine similarity is then used to find the most relevant document chunk.

### 5. Answer Generation

The system generates an answer using the retrieved passage.

The source page is also displayed so that the answer can be traced back to
the original document.

## Example

Question:

What are the working hours of the Student Support Desk?

The system retrieves the relevant passage, generates an answer, and displays the source page.

## Testing

The system was tested using eight questions based on the source document.

The test set includes:
- Questions that can be answered from the document
- Questions about specific sections and FAQs
- One question that cannot be answered from the document

The unanswerable question asks for the name of the current community lead, which is not specified in the source document.

## Experiments

Two chunking configurations were compared:

### Configuration 1

- Chunk size: 100
- Overlap: 20

### Configuration 2

- Chunk size: 200
- Overlap: 40

Smaller chunks provide more focused passages but can split related information.

Larger chunks preserve more surrounding context but may include additional information.

The observations and technical decision are documented in `DECISIONS.md`.

## Current Limitation

The current prototype uses a simple retrieval-based answer generation approach.

It retrieves the most relevant passage and selects the most relevant sentence from that passage. A full generative LLM can be added in a future version for more natural answers while keeping the answer grounded in retrieved context.


## Current Limitation

The final evaluation requires the document supplied for the GDG-USAR task.
The task description available during development did not include the
document itself.

## Future Improvements

- Add a graphical user interface
- Support multiple documents
- Improve answer generation using an LLM
- Add conversation history
- Improve retrieval using a vector database