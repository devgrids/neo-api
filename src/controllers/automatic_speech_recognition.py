from ai.automatic_speech_recognition.facebook_automatic_speech_recognition import FacebookAutomaticSpeechRecognition
from flask import jsonify, request

automatic_speech_recognition = FacebookAutomaticSpeechRecognition()

def handle():  
    try:
        data = request.get_json()
        base64 = data['base64']
        result = automatic_speech_recognition.generate(base64)        
        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"data": str(e)})
    
