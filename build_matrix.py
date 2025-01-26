import os
import numpy as np
from tokenizator import token
from detect_file_encoding import detect_file_encoding

def columns(dir):

    ponderated_matrix = []
    files_in_dir = []

    try:
        files_in_dir = os.listdir(dir)
    except FileNotFoundError:
        print(f"El directorio '{dir}' no existe.")
        return ponderated_matrix, files_in_dir, []

    all_tokens = set()

    for file_name in files_in_dir:
        file_path = os.path.join(dir, file_name)

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
    return columns, files_in_dir

def vector_file(dir, columns, files_dir):
    ponderated_matrix = []

    for file_name in files_dir:
        file_path = os.path.join(dir, file_name)

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
            
    return ponderated_matrix

def build_binary_matrix(search_dir):
    columnas, files_in_dir = columns(search_dir)
    ponderated_matrix = vector_file(search_dir, columnas, files_in_dir)
        
    return np.array(ponderated_matrix), columnas, files_in_dir