from rag.ingestion.loader import get_content
from rag.ingestion.cleaner import clean_content
from rag.ingestion.chunker import get_chunks

text = get_content()
cleaned_text = clean_content(text)
chunks = get_chunks(cleaned_text)

print(cleaned_text)
print(len(chunks))
print(chunks[0])