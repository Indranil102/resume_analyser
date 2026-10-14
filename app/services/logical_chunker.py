from langchain_core.documents import Document
from app.services.pdf_loader import load_pdf

from app.services.section_parser import split_into_sections
def split_experience(section:Document):
    text= section.page_content
    
    markers=[
        "AI/ML and Python Intern",
        "Software Developer Intern"
    ]
    
    chunks=[]
    
    current_content=[]
    
    for line in text.splitlines():
        line= line.strip()
        
        if not line:
            continue
        
        is_new_job= any(
            line.startswith(marker)
            for marker in markers
        )
        
        if is_new_job and current_content:
            chunks.append(
                Document(
                    page_content="\n".join(current_content),
                    metadata={
                        **section.metadata,
                        'subsection':'experience'
                    }
                )
            )
            
            current_content=[]
            
        current_content.append(line)
    if current_content:
        
        chunks.append(
            Document(
                page_content="\n".join(current_content),
                metadata={
                    **section.metadata,
                    'subsection':'experience'
                }
            )
        )
    return chunks

def split_projects(section: Document):
    
    text= section.page_content
    project_markers = [
        "Query Atlas",
        "Multi-Agent AI Research System",
        "Intelligent NLP-Based Meeting Scheduler"
    ]
    chunks=[]
    
    current_content=[]
    
    for line in text.splitlines():
        line= line.strip()
        
        if not line:
            continue
        is_new_project= any(
            line.startswith(marker)
            for marker in project_markers
        )
        
        if is_new_project and current_content:
            
            chunks.append(
                Document(
                    page_content="\n".join(current_content),
                    metadata={
                        **section.metadata,
                        'subsection':'projects'
                    }
                )
            )
            
            current_content=[]
            
            current_content.append(line)
    if current_content:
        chunks.append(
            Document(
                page_content="\n".join(current_content),
                metadata={
                    **section.metadata,
                    'subsection':'projects'
                }
            )
        )
        
    return chunks

def create_chunks(filepath:str):
    
    documents= load_pdf(filepath)
    
    all_chunks=[]
    
    for document in documents:
        sections= split_into_sections(document)
        
        for section in sections:
            section_name= section.metadata['section']
            
            if section_name== "EXPERIENCE":
                chunks= split_experience(section)
                
            elif section_name=="PROJECTS":
                chunks= split_projects(section)
            else:
                
                chunks=[section]
                
            all_chunks.extend(chunks)
            
    return all_chunks