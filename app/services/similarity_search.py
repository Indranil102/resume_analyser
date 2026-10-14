import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from app.services.embeddings import create_embeddings


def main():
    
    model= create_embeddings()
    
    query="Python machine learning experience"
    
    texts=[
        "Python developer with machine learning experience",
        "Experienced Python programmer working on ML projects",
        "I enjoy playing football",
    ]
    
    query_vector= model.embed_query(query)
    
    
    document_vectors= model.embed_documents(texts)
    
    scores= cosine_similarity(
        [query_vector],
        document_vectors
    )[0]
    results= sorted(zip(texts,scores),key= lambda item:item[1],reverse=True)
    
    print(f"Query: {query}\n")
    
    
    for rank,(text,score) in enumerate(results, start=1):
        
        
        print(f"Rank: {rank}")
       
        print(f"Text: {text}\n")
        
        print(f"Similarity Score: {score:.4f}")
        
if __name__=="__main__":
    main()