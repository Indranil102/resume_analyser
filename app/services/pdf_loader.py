import pymupdf  # PyMuPDF
from langchain_core.documents import Document
def load_pdf(file_path: str):
    """
    Load a PDF file and return its text content.

    Args:
        file_path (str): The path to the PDF file.
    """
    document = pymupdf.open(file_path)
    documents=[]
    for page_number ,page in enumerate(document):
        
        text = page.get_text()
        doc= Document(
            page_content=text,
            metadata={
                "source": file_path,
                "page_number": page_number + 1
            }
        )
        documents.append(doc)
        
        
    document.close()
    
    return documents
        
        
if __name__ == "__main__":
    documents= load_pdf("data/resumes/Indranil.pdf")
    
    for doc in documents:

        print("\n========== DOCUMENT ==========")

        print("CONTENT:")
        print(doc.page_content)

        print("\nMETADATA:")
        print(doc.metadata)