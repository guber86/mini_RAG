from pathlib import Path
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

BASE = Path(__file__).resolve().parents[2]

def get_database_path(filename: str = "database.txt") -> Path:
    path = BASE / "database" / filename

    return path

def save(vectors):
    path = get_database_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as database:
        for vector, text in vectors:
            vector_str = " ".join(map(str, vector))
            database.write(f"{vector_str};{text}\n")


def get_similar_chunks(vector, top_k=2):
    if top_k <=0:
        raise ValueError("top_k must be > 0")

    chunks = []
    path = get_database_path()

    with open(path, "r", encoding="utf-8") as database:
        for line in database:
            line = line.strip()
            if not line:
                continue
            else:
                [raw_vector, text] = line.split(";", 1)
                chunk_vector = np.array(raw_vector.split(), dtype=float)

            if chunk_vector.shape != vector.shape:
                raise ValueError("vectors must have same shape")
            else:
                score = cosine_similarity([chunk_vector], [vector])[0][0]
                chunks.append((text.strip(), float(score)))

    chunks.sort(key=lambda x: x[1], reverse=True)
    return chunks[:top_k]
