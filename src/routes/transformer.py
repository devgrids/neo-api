from flask import Blueprint
from controllers.transformer import generate_content

transformer_bp = Blueprint('transformer', __name__)

@transformer_bp.route('/generate_content', methods=['POST'])
def generate_content_api():  
    return generate_content()
