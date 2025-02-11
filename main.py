import os
import numpy as np
from tokenizator import token
from build_matrix import build_binary_matrix
from tools_pickle import save_binary_matrix, load_binary_matrix
from math_algorithm import search_similarity

def main():
    """
    Función principal que solicita al usuario una cadena de búsqueda y muestra los resultados.
    """
    search_dir = os.path.join(os.getcwd(), 'cadenas')
    pickle_dir = os.path.join(os.getcwd(), 'pickle')

    if not os.path.exists(pickle_dir):
        os.makedirs(pickle_dir)

    pickle_file_path = os.path.join(pickle_dir, 'binary_matrix.pickle')

    if not os.path.exists(pickle_file_path):
        matrix, columns, files = build_binary_matrix(search_dir)

        save_binary_matrix(matrix.tolist(), columns, files, pickle_dir)
    else:
        matrix, columns, files = load_binary_matrix(pickle_dir)

        matrix = np.array(matrix)

    user_input = input("Ingresa una cadena a buscar: ").strip()

    if not user_input:
        print("No ingresaste ninguna cadena. Terminando el programa.")
        return

    user_token = token(user_input)

    user_vector = [0] * len(columns)
    for word in user_token:
        if word in columns:
            user_vector[columns.index(word)] = 1

    user_vector = np.array([user_vector])

    similarity_results = search_similarity(user_vector, matrix, files)

    sorted_results = sorted(similarity_results.items(), key=lambda x: x[1], reverse=True)

    if sorted_results:
        print("\nResultados encontrados:")
        for file_name, data in sorted_results[:20]:
            print(f"Archivo: {file_name}")
            print(f"Similitud: {data:.2f}")
    else:
        print("No se encontraron resultados similares.")

if __name__ == "__main__":
    main()
