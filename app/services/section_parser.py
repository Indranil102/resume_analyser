import re
from app.services.pdf_loader import load_pdf
from langchain_core.documents import Document

SECTIONS=[
    "PROFESSIONAL SUMMARY",
    "SKILLS",
    "EXPERIENCE",
    "PROJECTS",
    "PUBLICATIONS",
    "LEADERSHIP & EXTRACURRICULAR",
    "EDUCATION",
]

def split_into_sections(document: Document):
    """
    Split a document into sections based on predefined section headers.

    Args:
        document (Document): The document to be split.

    Returns:
        List[Document]: A list of documents, each representing a section.
    """
    text= document.page_content
    sections=[]
    current_section="HEADER"
    current_content=[]
    
    lines=text.splitlines()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line in SECTIONS:
            if current_content:
                sections.append(
                    Document(
                        page_content="\n".join(current_content),
                        metadata={
                            **document.metadata,
                            "section": current_section
                        }
                    )
                )
            current_section=line
            current_content=[]
        else:
            current_content.append(line)
    if current_content:
        sections.append(
            Document(
                page_content='\n'.join(current_content),
                metadata={
                    **document.metadata,
                    "section": current_section
                }
            )
        )
    return sections

if __name__ == "__main__":

    documents = load_pdf("data/resumes/Indranil.pdf")

    sections = split_into_sections(documents[0])

    print(f"Total sections: {len(sections)}")

    for i, section in enumerate(sections):

        print(f"\n========== SECTION {i + 1} ==========")

        print("SECTION:", section.metadata["section"])
        
        print("CHARACTERS:", len(section.page_content))

        print("\nCONTENT:")

        print(section.page_content)