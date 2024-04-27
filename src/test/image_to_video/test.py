from diffusers import DiffusionPipeline
from PIL import Image
import torch

# Verificar si CUDA está disponible
if torch.cuda.is_available():
    # Imprimir el número de GPUs disponibles
    print(torch.cuda.device_count(), "GPU(s) disponibles.")
    # Imprimir el nombre de la GPU actual
    print("GPU actual:", torch.cuda.get_device_name(0))
else:
    print("CUDA no está disponible. Usando CPU.")

# Crear un objeto DiffusionPipeline cargando el modelo preentrenado
pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid-xt-1-1")

# Cargar la imagen de entrada
input_image_path = "assets/images/sera.png"
input_image = Image.open(input_image_path)

# Redimensionar y convertir la imagen
input_image = input_image.resize((16, 16))  # Redimensionar a un tamaño más pequeño
input_image = input_image.convert("RGB")  # Convertir a formato RGB

# Generar el video a partir de la imagen
video = pipeline(input_image)

# Guardar el video resultante
output_video_path = "video_salida.mp4"
video.save(output_video_path)

print("Video guardado en:", output_video_path)
