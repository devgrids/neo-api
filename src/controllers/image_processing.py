from ai.image_processing.gemini_image_processing import GeminiImageProcessing
from helpers.base64_to_image import base64_to_image
from flask import jsonify, request

image_processing = GeminiImageProcessing()

def send_message():  
    try:
        data = request.get_json()
        message = data['message']
        base64 = data['base64']
        image = base64_to_image(base64)  
        result = image_processing.send_message(message, image)
        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"data": str(e)})
    
    