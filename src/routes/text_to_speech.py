from flask import Blueprint
from controllers.text_to_speech import handle

text_to_speech_bp = Blueprint('text_to_speech', __name__)

@text_to_speech_bp.route('/', methods=['POST'])
def handle_api():
    return handle()
