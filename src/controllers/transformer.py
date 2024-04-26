from ai.transformer.gemini_transformer import GeminiTransformer
from flask import jsonify, request

transformer = GeminiTransformer()

def generate_content():  
    try:
        data = request.get_json()
        message = data['message']
        result = transformer.generate_content(message)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})

