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
                
So for our project, we'll use:
Rules first
+
Recursive splitter as fallback
+
LLM only when genuinely useful

step 5 pip install sentence-transformers