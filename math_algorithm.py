from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def search_similarity(user_input_vector, matrix, files):
    """
    Busca archivos en la matriz de similitudes que coincidan con el vector de entrada del usuario.

    Args:
        user_input_vector (np.ndarray): Vector que representa las características del input del usuario.
        matrix (np.ndarray): Matriz que contiene las características de los archivos a comparar.
        files (list): Lista de nombres de los archivos correspondientes a las filas de la matriz.

    Returns:
        dict: Un diccionario donde cada clave es el nombre de un archivo que supera el umbral de similitud,
              y cada valor es otro diccionario que contiene:
              - "similarity": El valor de similitud entre el input del usuario y el archivo.
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