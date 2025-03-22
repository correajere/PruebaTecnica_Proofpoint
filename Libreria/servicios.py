import pandas as pd

def leer_csv(ruta_archivo):
    """
    Lee un archivo CSV y lo carga en un DataFrame.
    """
    try:
        catalogo = pd.read_csv(ruta_archivo, header=None, names=["Título", "Autor", "Año de Publicación"])
        return catalogo
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return None

def limpiar_datos(catalogo):
    """
    Limpia los datos del catálogo:
    - Elimina filas con títulos faltantes.
    - Rellena autores faltantes con "Autor Desconocido".
    - Corrige años de publicación inválidos.
    """
    if catalogo is not None:
        # Eliminar filas con títulos faltantes
        catalogo.dropna(subset=["Título"], inplace=True)

        # Rellenar autores faltantes con "Autor Desconocido"
        catalogo.loc[:, "Autor"] = catalogo["Autor"].fillna("Autor Desconocido")

        # Corregir años de publicación inválidos
        catalogo.loc[:, "Año de Publicación"] = pd.to_numeric(catalogo["Año de Publicación"], errors="coerce")
        catalogo.loc[:, "Año de Publicación"] = catalogo["Año de Publicación"].apply(
            lambda x: x if pd.notna(x) and 0 < x <= 2025 else 0
        )

    return catalogo

def eliminar_duplicados(catalogo):
    """
    Elimina entradas duplicadas basadas en el título y el autor.
    """
    if catalogo is not None:
        catalogo.drop_duplicates(subset=["Título", "Autor"], keep="first", inplace=True)
    return catalogo

def organizar_datos(catalogo):
    """
    Ordena el catálogo por autor y año de publicación.
    """
    if catalogo is not None:
        catalogo.sort_values(by=["Autor", "Año de Publicación"], inplace=True)
    return catalogo