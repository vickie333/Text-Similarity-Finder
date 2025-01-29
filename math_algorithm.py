from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search_similarity(user_input_vector, matrix, files):
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

    results = {}
    for idx, similarity in enumerate(user_similarity):
        if similarity > threshold:
            results[files[idx]] = {
                "similarity": similarity
            }
    return results