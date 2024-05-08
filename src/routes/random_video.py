from flask import Blueprint
from controllers.random_video import handle

random_video_bp = Blueprint('random_video', __name__)

@random_video_bp.route('/', methods=['POST'])
def handle_api():
    return handle()
