from ai.vision_transformer.gemini_vision_transformer import GeminiVisionTransformer
from helpers.base64_to_image import base64_to_image
from flask import jsonify, request

vision_transformer = GeminiVisionTransformer()

def generate_content():  
    try:
        data = request.get_json()
        base64 = data['base64']
        image = base64_to_image(base64)  
        result = vision_transformer.generate_content(image)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})
