from ai.translate.helsinki_translate import *
from flask import jsonify, request

translate_spanish_to_english_ = HelsinkiTranslate(LanguageType.SPANISH_TO_ENGLISH)
translate_english_to_spanish_ = HelsinkiTranslate(LanguageType.ENGLISH_TO_SPANISH)

def translate_spanish_to_english():  
    try:
        data = request.get_json()
        message = data['message']
        result = translate_spanish_to_english_.translation(message)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})

def translate_english_to_spanish():  
    try:
        data = request.get_json()
        message = data['message']
        result = translate_english_to_spanish_.translation(message)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"result": str(e)})
    

    

