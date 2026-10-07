from langchain_core.documents import Document

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