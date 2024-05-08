from ai.text_to_image.dreamlike_art.diffusion_dreamlike_art_text_to_image import DiffusionDreamlikeArtTextToImage
from flask import jsonify, request
from helpers.image_to_base64 import image_to_base64


text_to_image = DiffusionDreamlikeArtTextToImage()

def generate():  
    try:
        data = request.get_json()
        prompt = data['prompt']
        params = data['params']
        images = text_to_image.generate(prompt, params)
        
        base64_images = []
        for image in images:
            base64 = image_to_base64(image)
            base64_images.append(base64)

        return jsonify({"data": base64_images})
    except Exception as e:
        return jsonify({"data": str(e)})
    

    

