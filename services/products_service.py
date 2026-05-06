import json
import os


def load_products():
    """
        Carga los productos desde el archivo JSON
        Devuelve una lista de diccionarios
    """
    
    base_path = os.path.dirname(os.path.dirname(__file__)) #Carpeta raíz del proyecto
    file_path = os.path.join(base_path, "data", "products.json") #Ruta completa del archivo

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            products = json.load(file)
            return products
    except FileNotFoundError:
        raise Exception("El archivo products.json no existe")
    except json.JSONDecodeError:
        raise Exception("El archivo products.json no es válido")
    except Exception as e:
        raise Exception(f"Error inesperado al cargar productos: {e}")
