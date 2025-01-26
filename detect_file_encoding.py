import chardet

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