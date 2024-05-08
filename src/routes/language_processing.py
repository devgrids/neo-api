from flask import Blueprint
from controllers.language_processing import send_message

language_processing_bp = Blueprint('language_processing', __name__)

@language_processing_bp.route('/send_message', methods=['POST'])
def send_message_api():
    return send_message()
