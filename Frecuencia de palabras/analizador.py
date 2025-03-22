import re
from collections import Counter

def limpiar_texto(texto):
    """
    Limpia el texto: elimina signos de puntuación y convierte a minúsculas.
    """
    texto_limpio = re.sub(r'[^\w\s]', '', texto)  # Eliminar signos de puntuación
    texto_limpio = texto_limpio.lower()  # Convertir a minúsculas
    return texto_limpio

def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto.
    """
    palabras = texto.split()
    return Counter(palabras)

def obtener_palabras_mas_frecuentes(contador, n=10):
    """
    Devuelve las n palabras más frecuentes.
    """
    return contador.most_common(n)