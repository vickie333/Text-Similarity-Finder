# README

## Descripción

Este proyecto permite buscar cadenas de texto similares dentro de un conjunto de archivos de texto ubicados en la carpeta `cadenas`. Convierte los archivos en una matriz binaria de presencia/ausencia de palabras (tokens) y, para una consulta del usuario, calcula la similitud del coseno entre la consulta y cada archivo. Muestra los archivos más similares junto con un puntaje de similitud.

## ¿Cómo funciona?

- Tokenización: `tokenizator.py` divide el texto en tokens usando una lista de delimitadores.
- Construcción de matriz:
  - `build_matrix.columns(dir)`: recorre los archivos de `cadenas`, detecta su codificación con `detect_file_encoding.py` (usa `chardet`) y extrae el conjunto de tokens únicos (columnas).
  - `build_matrix.vector_file(dir, columns, files)`: construye una matriz binaria (1 si el token aparece en el archivo, 0 si no).
  - `build_matrix.build_binary_matrix(search_dir)`: devuelve `matrix` (NumPy), `columns` y `files`.
- Caché de resultados: la primera vez guarda `matrix`, `columns` y `files` en `pickle/binary_matrix.pickle` usando `tools_pickle.py`. En ejecuciones posteriores, los carga para evitar recomputar.
- Búsqueda: en `main.py`, tu consulta se tokeniza y se convierte en un vector binario alineado con `columns`.
- Similitud: `math_algorithm.search_similarity` calcula la similitud del coseno entre tu vector y cada fila de `matrix`. Solo devuelve resultados por encima del umbral, que es la media de similitudes de esa consulta.

## Requisitos

- Python 3.9+
- Dependencias: instala con:

```bash
pip install -r requirements.txt
```

## Instalación y uso

1) Coloca tus archivos de texto dentro de una carpeta llamada `cadenas` en el directorio del proyecto.
   - Si no existe, créala (el proyecto también creará automáticamente la carpeta `pickle` para la caché).
2) Ejecuta el programa:

```bash
python main.py
```

3) Escribe en la terminal la cadena a buscar cuando se te solicite.
4) Verás los resultados ordenados por similitud (se muestran hasta 20).

## Estructura del proyecto

- `main.py`: orquesta el flujo, gestiona la caché y muestra resultados.
- `build_matrix.py`: construye las columnas (tokens) y la matriz binaria por archivo.
- `tokenizator.py`: tokeniza texto con delimitadores predefinidos.
- `detect_file_encoding.py`: detecta codificación de archivos con `chardet`.
- `math_algorithm.py`: calcula similitud de coseno y filtra por umbral (media).
- `tools_pickle.py`: guarda y carga `binary_matrix.pickle` en la carpeta `pickle`.

## Ejemplo de salida

```
Resultados encontrados:
Archivo: documento1.txt
Similitud: 0.72
Archivo: notas_proyecto.md
Similitud: 0.65
...
```

## Personalización

- Carpeta de búsqueda: por defecto es `./cadenas`. Puedes modificar `search_dir` en `main.py` si necesitas otra ruta.
- Umbral de similitud: actualmente es la media de similitudes de la consulta. Puedes cambiar la lógica en `math_algorithm.py` (por ejemplo, fijar un umbral absoluto como 0.2).
- Número de resultados: en `main.py` se muestran los primeros 20; ajusta el slicing `[:20]` si deseas más o menos.

## Notas y buenas prácticas

- Formato de archivos: se recomienda texto plano. El proyecto detecta codificación automáticamente, pero archivos binarios o muy grandes pueden fallar.
- Rendimiento: la primera ejecución puede tardar más al construir la matriz; luego, la carga desde `pickle` es rápida.
- Normalización: todo el texto se pasa a minúsculas para que la coincidencia sea insensible a mayúsculas.

## Solución de problemas

- No se encuentran resultados:
  - Asegúrate de tener archivos en `cadenas` y que contengan tokens similares a tu consulta.
  - Intenta consultas más generales o modifica el umbral en `math_algorithm.py`.
- Errores de lectura de archivos:
  - Revisa mensajes sobre codificación en consola. El detector usa `chardet`; si falla, convierte el archivo a UTF-8.
- Caché desactualizada:
  - Si agregas/eliminás muchos archivos en `cadenas`, borra `pickle/binary_matrix.pickle` para forzar la reconstrucción.

## Licencia

Consulta el archivo `LICENSE` incluido en este repositorio.