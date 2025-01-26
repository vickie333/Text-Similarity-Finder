from pickle import dump, load
import os

def save_binary_matrix(matrix, columns, files, search_dir):
    """
    Guarda la matriz binaria, columnas y archivos en un archivo.

    Args:
        matrix (list): Matriz binaria de características.
        columns (list): Lista de las columnas (palabras) correspondientes.
        files (list): Lista de nombres de los archivos correspondientes.
        search_dir (str): Ruta del directorio donde se guardarán los archivos.
    """
    try:
        with open(os.path.join(search_dir, 'binary_matrix.pickle'), 'wb') as f:
            dump((matrix, columns, files), f)
    except Exception as e:
        print(f"Error al guardar la matriz binaria: {e}")


def load_binary_matrix(search_dir):
    """
    Carga la matriz binaria, columnas y archivos desde un archivo.

    Args:
        search_dir (str): Ruta del directorio donde se encuentra el archivo.

    Returns:
        tuple: (matrix, columns, files) - La matriz binaria, las columnas y los archivos.
    """
    try:
        with open(os.path.join(search_dir, 'binary_matrix.pickle'), 'rb') as f:
            matrix, columns, files = load(f)
            return matrix, columns, files
    except Exception as e:
        print(f"Error al cargar la matriz binaria: {e}")
        return [], [], []
