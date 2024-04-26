from flask import Blueprint
from controllers.chat import send_message

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/send_message', methods=['POST'])
def send_message_api():  
    return send_message()
