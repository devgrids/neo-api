from ai.chat_vision.gemini_chat_vision import GeminiChatVision
from helpers.base64_to_image import base64_to_image
from flask import jsonify, request

chat_vision = GeminiChatVision()

def send_message():  
    try:
        data = request.get_json()
        message = data['message']
        base64 = data['base64']
        image = base64_to_image(base64)  
        result = chat_vision.send_message(message, image)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})
    

    

