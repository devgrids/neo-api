from flask import Flask
from flask_cors import CORS

from routes.translate import translate_bp
from routes.language_processing import language_processing_bp
from routes.image_processing import image_processing_bp
from routes.random_image import random_image_bp
from routes.random_video import random_video_bp
from routes.text_to_image import text_to_image_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(translate_bp, url_prefix='/translate')
app.register_blueprint(language_processing_bp, url_prefix='/language_processing')
app.register_blueprint(image_processing_bp, url_prefix='/image_processing')
app.register_blueprint(random_image_bp, url_prefix='/random_image')
app.register_blueprint(random_video_bp, url_prefix='/random_video')
app.register_blueprint(text_to_image_bp, url_prefix='/text_to_image')

# Root route
@app.route('/')
def root():
    return 'Neo API!'

if __name__ == '__main__':
    app.run(debug=True)
