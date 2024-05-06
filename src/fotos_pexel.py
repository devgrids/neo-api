import requests
import os

def buscar_imagenes(query, cantidad):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={cantidad}"
    headers = {"Authorization": os.environ.get("PEXEL_API_KEY")}
    respuesta = requests.get(url, headers=headers)
    if respuesta.status_code == 200:
        return respuesta.json()['photos']
    else:
        print("Error al buscar imágenes:", respuesta.text)
        return None

def descargar_imagenes(imagenes, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    for i, imagen in enumerate(imagenes):
        url = imagen['src']['original']
        nombre_archivo = os.path.join(carpeta_destino, f"imagen_{i+1}.jpg")
        try:
            with open(nombre_archivo, 'wb') as archivo:
                respuesta = requests.get(url)
                archivo.write(respuesta.content)
            print(f"Imagen {nombre_archivo} descargada correctamente.")
        except Exception as e:
            print(f"Error al descargar la imagen {nombre_archivo}: {e}")

if __name__ == "__main__":
    query = input("Ingrese el término de búsqueda para las imágenes: ")
    cantidad = int(input("Ingrese la cantidad de imágenes que desea descargar: "))

    imagenes = buscar_imagenes(query, cantidad)
    if imagenes:
        carpeta_destino = "imagenes"
        descargar_imagenes(imagenes, carpeta_destino)
