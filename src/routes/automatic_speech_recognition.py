from flask import Blueprint
from controllers.automatic_speech_recognition import handle

automatic_speech_recognition_bp = Blueprint('automatic_speech_recognition', __name__)

@automatic_speech_recognition_bp.route('/', methods=['POST'])
def handle_api():
    return handle()
