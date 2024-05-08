from flask import Blueprint
from controllers.random_image import handle

random_image_bp = Blueprint('random_image', __name__)

@random_image_bp.route('/', methods=['POST'])
def handle_api():
    return handle()
