from flask import Blueprint
from controllers.chat_vision import send_message

chat_vision_bp = Blueprint('chat_vision', __name__)

@chat_vision_bp.route('/send_message', methods=['POST'])
def send_message_api():  
    return send_message()
