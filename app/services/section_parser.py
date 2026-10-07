import re

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
    current_section="Header"
    current_content=[]
    
    lines=text.splitlines()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line in S

    