from ai.text_to_speech.google_text_to_speech import GoogleTextToSpeech
from flask import jsonify, request

text_to_speech = GoogleTextToSpeech()

def handle():  
    try:
        data = request.get_json()
        text = data['text']
        language = data['language']
        result = text_to_speech.generate(text, language)     
        return jsonify({"data": result})
    except Exception as e:
        return jsonify({"data": str(e)})
    
