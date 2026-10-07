# Resume Analyser

## Setup

Activate the Conda environment:

```bash
conda activate resume-analyser
```

Install project dependencies after adding them to `requirements.txt`:

```bash
pip install -r requirements.txt
```
currently in text_spliiter file i am working with this 
                         PDF
                          ↓
                       PyMuPDF
                          ↓
                    LangChain Document
                          ↓
                    Section Detection
                          ↓
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
       Skills         Experience       Projects
          ↓               ↓               ↓
       Document        Document        Document
          │               │               │
          └───────────────┼───────────────┘
                          ↓
               Recursive Splitter
              only if section is large
                          ↓
                       Chunks
                