from ai.language_processing.gemini_language_processing import GeminiLanguageProcessing
from flask import jsonify, request

language_processing = GeminiLanguageProcessing()

def send_message():  
    try:
        data = request.get_json()
        message = data['message']
        result = language_processing.send_message(message)
        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"data": str(e)})
    
