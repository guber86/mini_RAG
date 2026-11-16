from rag.ingestion.loader import get_content
from rag.ingestion.cleaner import clean_content
from rag.ingestion.chunker import get_chunks
from rag.ingestion.embedder import get_vectors, get_vector

text = get_content()
cleaned_text = clean_content(text)
chunks = get_chunks(cleaned_text)

vector = get_vector("Как оплатить заказ?")
vectors = get_vectors(chunks)

print(vectors[0][1])
print(len(vectors))
print(vectors[0][0].shape)
print(vector.shape)