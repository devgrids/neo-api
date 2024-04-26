from PIL import Image
from io import BytesIO
import base64

def base64_to_image(bits):
    data = base64.b64decode(bits)
    image = Image.open(BytesIO(data))
    return image
