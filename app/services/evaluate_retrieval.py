from langchain_community.vectorstores import FAISS

from app.services.embeddings import create_embeddings
from app.services.evalution_dataset import EVALUATION_DATASET

INDEX_PATH="data/faiss_index"

def is_relevant(document,item):
    
    metadata= document.metadata
    
    relevant_sections= item.get("relevant_sections",[])
    relevant_projects= item.get("relevant_projects",[])
    relevant_companies= item.get("relevant_companies",[])
    
    return (
        metadata.get("section") in relevant_sections or
        metadata.get("project") in relevant_projects or
        metadata.get("company") in relevant_companies
    )
    
def evaluate_query(vector_store, item, k):
    results= vector_store.similarity_search_with_score(
        item['query'], k=k
    )
    
    relevant_count= sum(
        is_relevant(document,item)
        for document, distance  in results
    )
    
    precision= relevant_count/ len(results) if results else 0.0
    
    all_documents= vector_store.similarity_search(item['query'], k=vector_store.index.ntotal)
    
    total_relevant= sum(
        is_relevant(document,item)
        for document in all_documents
    )
    
    recall= (
        relevant_count/ total_relevant
        if total_relevant>0 else 0.0
    )
    
    reciprocal_rank= 0.0
    
    for rank, (document, distance) in enumerate(results, start=1):
        if is_relevant(document, item):
            reciprocal_rank=1/rank
            break
    return precision, recall, reciprocal_rank, results


def main():
    embedding_model = create_embeddings()

    vector_store = FAISS.load_local(
        INDEX_PATH,
        embedding_model,
        allow_dangerous_deserialization=True,
    )

    for k in [3, 5]:
        precisions = []
        recalls = []
        reciprocal_ranks = []

        print(f"\n{'=' * 60}")
        print(f"EVALUATION AT K = {k}")
        print("=" * 60)

        for item in EVALUATION_DATASET:
            precision, recall, rr, results = evaluate_query(
                vector_store,
                item,
                k,
            )

            precisions.append(precision)
            recalls.append(recall)
            reciprocal_ranks.append(rr)

            print(f"\nQuery: {item['query']}")
            print(f"Precision@{k}: {precision:.3f}")
            print(f"Recall@{k}: {recall:.3f}")
            print(f"Reciprocal Rank: {rr:.3f}")

            print("Retrieved chunks:")
            for rank, (document, distance) in enumerate(
                results, start=1
            ):
                print(
                    f"{rank}. "
                    f"Section={document.metadata.get('section')}, "
                    f"Project={document.metadata.get('project')}, "
                    f"Company={document.metadata.get('company')}, "
                    f"Distance={distance:.4f}"
                )

        print("\nAVERAGE METRICS")
        print(f"Mean Precision@{k}: {sum(precisions) / len(precisions):.3f}")
        print(f"Mean Recall@{k}: {sum(recalls) / len(recalls):.3f}")
        print(f"MRR@{k}: {sum(reciprocal_ranks) / len(reciprocal_ranks):.3f}")


if __name__ == "__main__":
    main()

