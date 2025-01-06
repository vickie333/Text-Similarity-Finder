import os
import chardet
from difflib import SequenceMatcher

def detect_file_encoding(file):
    """
    Detecta la codificación de un archivo.

    Args:
        file (str): Archivo.

    Returns:
        str: Codificación detectada o 'utf-8' como valor predeterminado.
    """
    try:
        with open(file, 'rb') as f:
            resultado = chardet.detect(f.read())
            encoding = resultado['encoding']
            return encoding or 'utf-8'
    except Exception as e:
        print(f"No se pudo leer el archivo: {file}: {e}")
        return 'utf-8'

def search_string_in_files(search_dir, search_string, similarity_threshold=0.7):
    """
    Busca una cadena completa o similar en los archivos de texto de un directorio.

    Args:
        search_dir (str): Ruta del directorio donde buscar.
        search_string (str): Cadena completa a buscar.
        similarity_threshold (float): Umbral de similitud (0 a 1).

    Returns:
        list: Lista de resultados con archivo, línea y contenido donde se encuentra la coincidencia o algo similar.
    """
    results = []

    try:
        files_in_dir = os.listdir(search_dir)
    except FileNotFoundError:
        print(f"El directorio '{search_dir}' no existe.")
        return results

    for file_name in files_in_dir:
        file_path = os.path.join(search_dir, file_name)

        if not os.path.isfile(file_path):
            continue
        
        encoding = detect_file_encoding(file_path)

        try:
            with open(file_path, 'r', encoding=encoding) as file:
                for line_num, line in enumerate(file, start=1):
                    if search_string in line:
                        results.append((file_path, line_num, line.strip(), "Coincidencia exacta"))
                    else:
                        words = line.strip().split()
                        for word in words:
                            similarity = SequenceMatcher(None, search_string, word).ratio()
                            if similarity >= similarity_threshold:
                                results.append((file_path, line_num, line.strip(), f"Similitud: {similarity:.2f}"))
        except Exception as e:
            print(f"Error al leer el archivo {file_path}: {e}")
    
    return results

def main():
    """
    Función principal que solicita al usuario una cadena de búsqueda y muestra los resultados.
    """
    search_dir = os.path.join(os.getcwd(), 'cadenas')

    if not os.path.exists(search_dir):
        print(f"El directorio '{search_dir}' no existe. Créalo y coloca archivos para analizar.")
        return

    user_input = input("Ingresa una cadena a buscar: ").strip()

    if not user_input:
        print("No ingresaste ninguna cadena. Terminando el programa.")
        return

    results = search_string_in_files(search_dir, user_input)

    if results:
        print(f"\nSe encontraron {len(results)} coincidencias:")
        for file_path, line_num, line, reason in results:
            print(f"- Archivo: {file_path}, Línea: {line_num}, Contenido: '{line}' ({reason})")
    else:
        print("No se encontraron resultados.")

main()