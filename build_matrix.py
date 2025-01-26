import os
import numpy as np
from tokenizator import token
from detect_file_encoding import detect_file_encoding

def build_binary_matrix(search_dir):
    """
    Construye una matriz binaria que indica la presencia de palabras en los archivos de un directorio.

    Args:
        search_dir (str): Ruta del directorio donde buscar.

    Returns:
        tuple: Una matriz binaria, una lista de nombres de archivos y una lista de palabras (columnas).
    """
    ponderated_matrix = []
    files_in_dir = []

    try:
        files_in_dir = os.listdir(search_dir)
    except FileNotFoundError:
        print(f"El directorio '{search_dir}' no existe.")
        return ponderated_matrix, files_in_dir, []

    all_tokens = set()

    for file_name in files_in_dir:
        file_path = os.path.join(search_dir, file_name)

        if not os.path.isfile(file_path):
            continue

        try:
            with open(file_path, 'r', encoding=detect_file_encoding(file_path)) as file:
                content = file.read().lower()
                tokens = token(content)

                all_tokens.update(tokens)

        except Exception as e:
            print(f"Error procesando el archivo {file_path}: {e}")

    columns = sorted(all_tokens)

    for file_name in files_in_dir:
        file_path = os.path.join(search_dir, file_name)

        if not os.path.isfile(file_path):
            continue

        try:
            with open(file_path, 'r', encoding=detect_file_encoding(file_path)) as file:
                content = file.read().lower()
                tokens = token(content)

                file_vector = [0] * len(columns)

                present_tokens = set(tokens)

                for idx, word in enumerate(columns):
                    if word in present_tokens:
                        file_vector[idx] = 1

                ponderated_matrix.append(file_vector)

        except Exception as e:
            print(f"Error procesando el archivo {file_path}: {e}")
        except (OSError, IOError) as e:
            print(f"Error al leer el archivo {file_path}: {e}")

    columns = sorted(all_tokens)

    return np.array(ponderated_matrix), columns, files_in_dir
