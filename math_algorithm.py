from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search_similarity(user_input_vector, matrix, files, columns):
    """
    Función que busca en la matriz de similitudes los archivos que coincidan con la entrada del usuario.

    Args:
        user_input_vector: Vector de características del input del usuario.
        matrix: Matriz de características de los archivos.
        files: Lista de nombres de los archivos.

    Returns:
        dict: Diccionario con los nombres de los archivos, su similitud, y palabras relevantes.
    """

    user_similarity = cosine_similarity(user_input_vector, matrix).flatten()

    threshold = np.mean(user_similarity)
    print(f"Umbral dinámico calculado: {threshold:.2f}")

    results = {}
    for idx, similarity in enumerate(user_similarity):
        if similarity > threshold:
            relevant_word_indices = matrix[idx].nonzero()[0].tolist()
            relevant_words = [columns[i] for i in relevant_word_indices]
            results[files[idx]] = {
                "similarity": similarity,
                "relevant_words": relevant_words
            }
    return results