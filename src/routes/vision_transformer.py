from flask import Blueprint
from controllers.vision_transformer import generate_content

vision_transformer_bp = Blueprint('vision_transformer', __name__)

@vision_transformer_bp.route('/generate_content', methods=['POST'])
def generate_content_api():  
    return generate_content()
