from flask import Blueprint
from controllers.translate import *

translate_bp = Blueprint('translate', __name__)

@translate_bp.route('/spanish_to_english', methods=['POST'])
def translate_spanish_to_english_api():  
    return translate_spanish_to_english()

@translate_bp.route('/english_to_spanish', methods=['POST'])
def translate_english_to_spanish_api():  
    return translate_english_to_spanish()
