from flask import Blueprint
from controllers.text_to_image import generate

text_to_image_bp = Blueprint('text_to_image', __name__)

@text_to_image_bp.route('/generate', methods=['POST'])
def generate_api():
    return generate()
