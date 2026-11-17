import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from rag.ingestion.repository import save, get_similar_chunks

vector_1 = [np.array([0.0, 1.0]), "Первый"]
vector_2 = [np.array([1.0, 0.0]), "Второй"]
vector_3 = [np.array([0.8, 0.6]), "Третий"]

vectors = [vector_1, vector_2, vector_3]
query = np.array([1.0, 0.0])

scores = []
for vector in vectors:
    score = cosine_similarity([query], [vector[0]])[0][0]
    scores.append(score)

print(scores)

sorted_scores_desc = np.argsort(scores)[:: -1]
top_k_indices = sorted_scores_desc[: 2]

print(top_k_indices)





