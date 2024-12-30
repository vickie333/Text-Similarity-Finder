import os
from fuzzywuzzy import fuzz

def search_approx_string_in_files(search_dir, search_string, threshold=60):
    """
    Busca una cadena en archivos de texto usando coincidencias aproximadas.

    Args:
        search_dir (str): Ruta del directorio donde buscar.
        search_string (str): Cadena a buscar.
        threshold (int): Puntuación mínima de similitud (0-100) para considerar una coincidencia.

    Returns:
        list: Lista de resultados con archivo, línea, posición y similitud.
    """
    results = []

    try:
        files_in_dir = os.listdir(search_dir)
    except FileNotFoundError:
        print(f"El directorio '{search_dir}' no existe.")
        return results

    for file_name in files_in_dir:
        file_path = os.path.join(search_dir, file_name)

        # Procesar solo archivos de texto
        if not os.path.isfile(file_path):
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, start=1):
                    words = line.split()  # Dividir la línea en palabras para comparar
                    for word in words:
                        similarity = fuzz.ratio(search_string.lower(), word.lower())
                        if similarity >= threshold:
                            results.append((file_path, line_num, word, similarity))
        except (IOError, UnicodeDecodeError):
            print(f"No se pudo leer el archivo: {file_path}")

    return results


def main():
    # Directorio predeterminado
    search_dir = os.path.join(os.getcwd(), 'cadenas')

    # Obtener entrada del usuario
    user_input = input("Ingresa una palabra a buscar (búsqueda aproximada): ").strip()

    if not user_input:
        print("No ingresaste ninguna palabra. Terminando el programa.")
        return

    #


    results = search_approx_string_in_files(search_dir, user_input)

    if results:
        print(f"\nSe encontraron {len(results)} coincidencias aproximadas:")
        for file_path, line_num, word, similarity in results:
            print(f"- Archivo: {file_path}, Línea: {line_num}, Palabra: '{word}', Similitud: {similarity}%")
    else:
        print("No se encontraron resultados aproximados.")


if __name__ == '__main__':
    main()
