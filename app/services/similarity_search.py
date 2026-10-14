import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from app.services.embeddings import create_embeddings
from app.services.logical_chunker import create_chunks

def main():
    
    model= create_embeddings()
    
    query="Python machine learning experience"
    
    chunks= create_chunks("data/resumes/Indranil.pdf")
    query_vector= model.embed_query(query)
    
    
    document_vectors= model.embed_documents([chunk.page_content for chunk in chunks])
    
    scores= cosine_similarity(
        [query_vector],
        document_vectors
    )[0]
    results= sorted(zip(chunks,scores),key= lambda item:item[1],reverse=True)
    
    print(f"Query: {query}\n")
    
    
    for rank,(chunk,score) in enumerate(results, start=1):
        
        
        print(f"Rank: {rank}")
       
        print(f"Text: {chunk.page_content}\n")
        
        print(f"Similarity Score: {score:.4f}")
        
if __name__=="__main__":
    main()