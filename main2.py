from PyPDF2 import PdfReader

from docx import Document
import subprocess

# EXTRACT PDF TEXT
def extract_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# EXTRACT DOCX TEXT
def extract_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])
# CHUNKING (200 words)
def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks
# FIND BEST CHUNK (simple matching)
def find_best_chunk(chunks, query):
    query_words = query.lower().split()
    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        score = sum(word in chunk.lower() for word in query_words)
        if score > best_score:
            best_score = score
            best_chunk = chunk

    return best_chunk

# ASK LLAVA MODEL
def ask_llava(context, query):
    prompt = f"Use this context to answer:\n\n{context}\n\nQuestion: {query}"

    result = subprocess.run(
        ["ollama", "run", "llava"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()
# MAIN PIPELINE
# -----------------------------
def run_pipeline():
    # 1. Extract text from both files
    pdf_text = extract_pdf("doc1.pdf")
    docx_text = extract_docx("doc2.docx")

    # 2. Combine text
    full_text = pdf_text + "\n" + docx_text

    # 3. Chunk the text
    chunks = chunk_text(full_text)

    # 4. Ask user for question
    query = input("\nEnter your question: ")

    # 5. Find best chunk
    best_chunk = find_best_chunk(chunks, query)

    # 6. Ask LLAVA
    answer = ask_llava(best_chunk, query)

    print("\n----------------------------------")
    print("ANSWER:")
    print(answer)
    print("----------------------------------")


# Run pipeline
if __name__ == "__main__":
    run_pipeline()
