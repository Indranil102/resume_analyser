from langchain_core.documents import Document
from app.services.pdf_loader import load_pdf

from app.services.section_parser import split_into_sections


from langchain_core.documents import Document


def split_experience(section: Document):
    text = section.page_content

    markers = [
        "AI/ML and Python Intern",
        "Software Developer Intern",
    ]

    chunks = []
    current_content = []

    def save_chunk(lines):
        if not lines:
            return

        chunk_text = "\n".join(lines)

        if "Emeelan Solution" in chunk_text:
            company = "Emeelan Solution"
        elif "DevFrame Studio" in chunk_text:
            company = "DevFrame Studio"
        else:
            company = None

        role = lines[0]

        chunks.append(
            Document(
                page_content=chunk_text,
                metadata={
                    **section.metadata,
                    "subsection": "experience",
                    "role": role,
                    "company": company,
                },
            )
        )

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        is_new_job = any(
            line.startswith(marker)
            for marker in markers
        )

        if is_new_job and current_content:
            save_chunk(current_content)
            current_content = []

        current_content.append(line)

    # Save the final job
    save_chunk(current_content)

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
    current_project=None
    
    def save_chunk():
        if not current_content:
            return
        
        chunks.append(
            Document(
                page_content="\n".join(current_content),
                metadata={
                    **section.metadata,
                    'subsection':'projects',
                    "project": current_project
                }
            )
        )
    
    for line in text.splitlines():
        line= line.strip()
        
        if not line:
            continue
        matched_project= next(
            (
                marker
                for marker in project_markers
                if line.startswith(marker)
            ),
            None
        )
        if matched_project:
            save_chunk()
            current_content=[]
            current_project= matched_project
        current_content.append(line)
    
    
    save_chunk()
        
            
            
        
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


if __name__ == "__main__":
    from app.services.pdf_loader import load_pdf
    from app.services.section_parser import split_into_sections

    documents = load_pdf("data/resumes/Indranil.pdf")

    for document in documents:
        sections = split_into_sections(document)

        for section in sections:
            section_name = section.metadata["section"]

            if section_name == "EXPERIENCE":
                chunks = split_experience(section)

            elif section_name == "PROJECTS":
                chunks = split_projects(section)

            else:
                continue

            for chunk in chunks:
                print("\n" + "=" * 60)
                print("Metadata:", chunk.metadata)
                print(chunk.page_content)
