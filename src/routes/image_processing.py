from flask import Blueprint
from controllers.image_processing import send_message

image_processing_bp = Blueprint('image_processing', __name__)

@image_processing_bp.route('/send_message', methods=['POST'])
def send_message_api():
    return send_message()
