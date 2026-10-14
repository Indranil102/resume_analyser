from langchain_community.vectorstores import FAISS

from app.services.embeddings import create_embeddings

INDEX_PATH= "data/faiss_index"

def search_resume(query:str,top_k: int=5):
    """
    Search the FAISS vector store for relevant chunks based on the query.

    Args:
        query (str): The search query.
        top_k (int): The number of top results to return.
        """
        
    embedding_model = create_embeddings()
    
    # lead the previously saved index
    vector_store = FAISS.load_local(INDEX_PATH, embedding_model,allow_dangerous_deserialization=True,)
    
    #retrive the most relevent chunks
    
    result= vector_store.similarity_search_with_score(query, k=top_k)
    
    
    for rank, (document,distance) in enumerate(result,start=1):
        
        print("="*60)
        print(f"Rank: {rank}")
        print(f"FAISS Distance: {distance:.4f}")
        
        print(f"Metadata: {document.metadata}")
        print(f"Content: {document.page_content}")
        
        
if __name__ == "__main__":
    query = (
        "Experience building RAG applications using LangChain, "
        "vector databases, embeddings, Python and FastAPI"
    )

    search_resume(query)
