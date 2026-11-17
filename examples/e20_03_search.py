from rag.ingestion.embedder import get_vector
from rag.ingestion.repository import get_similar_chunks

question = "Можно ли оплатить заказ после получения?"

question_vector = get_vector(question)
similar_chunks = get_similar_chunks(question_vector)

for chunk in similar_chunks:
    print(f"Text: {chunk[0]}, Score: {float(chunk[1]):.4f}")