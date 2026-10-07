from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.services.pdf_loader import load_pdf
# we are loading the pdf file and then splitting the text into smaller chunks using the RecursiveCharacterTextSplitter class from langchain_text_splitter module. This is useful for processing large documents in smaller parts.


documents = load_pdf("data/resumes/Indranil.pdf")

splitter= RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)

chunks= splitter.split_documents(documents)

print(f"Total chuunks created: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n========== CHUNK {i+1} ==========")
    print("CONTENT:")
    print()
    print(chunk.page_content)
    print()
    print("\nMETADATA:")
    print(chunk.metadata)