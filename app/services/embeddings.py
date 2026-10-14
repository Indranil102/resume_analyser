from langchain_huggingface import HuggingFaceEmbeddings

def create_embeddings():
    """
    Create embeddings using the HuggingFaceEmbeddings class.
    """
    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )
    return model


if __name__=="__main__":
    model= create_embeddings()
    texts = [
        "Python developer with machine learning experience",
        "Experienced Python programmer working on ML projects",
        "I enjoy playing football"
    ]
    
    vectors= model.embed_documents(texts)
    for text, vector in zip(texts,vectors):
        print("===========TEXT===========")
        print(f"Text: {text}")
        print(f"Vector length: {len(vector)}")
        print("FIRST 5 values:")
        print(vector[:5])
        print()