from pathlib import Path

from langchain_community.vectorstores import FAISS

from app.services.embeddings import create_embeddings

from app.services.logical_chunker import create_chunks


RESUME_PATH= "data/resumes/Indranil.pdf"
INDEX_PATH= "data/faiss_index"


def build_vector_store():
    #1. Process the resume into logical chunks
    
    chunks = create_chunks(RESUME_PATH)
    
    if not chunks:
        raise ValueError("No chunks were created from the resume. Please check the input file.")
    print(f"Total chunks created: {len(chunks)}")
    
    embedding_model = create_embeddings()
    
    # 3. Embed chunks and build the FAISS index

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model,
    )
    
    
    Path(INDEX_PATH).mkdir(parents=True, exist_ok=True)
    vector_store.save_local(INDEX_PATH)
    
    print(f"FAISS index saved at: {INDEX_PATH}")
    print("Vector store building completed successfully.")
    
    return vector_store


if __name__ == "__main__":
    build_vector_store()