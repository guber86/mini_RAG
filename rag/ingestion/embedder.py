from sentence_transformers import SentenceTransformer

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"

model = SentenceTransformer(MODEL_NAME, device="cpu")

def get_vector(chunk):
    return model.encode(chunk, show_progress_bar=False)

def get_vectors(chunks):
    vectors = []
    for chunk in chunks:
        vector = get_vector(chunk)
        vectors.append([vector, chunk])

    return vectors
