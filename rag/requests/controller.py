from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks
from llm.llm import get_ai_response

def get(query, top_k=2, mode="demo"):
    query_vector = get_vector(query)
    chunks = get_similar_chunks(query_vector, top_k)
    response = get_ai_response(query, chunks, mode)
    return response
