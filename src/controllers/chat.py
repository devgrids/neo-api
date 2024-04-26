from ai.chat.gemini_chat import GeminiChat
from flask import jsonify, request

chat = GeminiChat()

def send_message():  
    try:
        data = request.get_json()
        message = data['message']
        result = chat.send_message(message)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})
    

    

