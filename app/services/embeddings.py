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
    mmodel= create_embeddings()
    texts = [
        "Python developer with machine learning experience",
        "Experienced Python programmer working on ML projects",
        "I enjoy playing football"
    ]