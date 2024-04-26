from flask import Flask
from flask_cors import CORS

from routes.vision_transformer import vision_transformer_bp
from routes.transformer import transformer_bp
from routes.translate import translate_bp
from routes.chat import chat_bp
from routes.chat_vision import chat_vision_bp

app = Flask(__name__)
CORS(app) 

# Register blueprints
app.register_blueprint(vision_transformer_bp, url_prefix='/vision_transformer')
app.register_blueprint(transformer_bp, url_prefix='/transformer')
app.register_blueprint(translate_bp, url_prefix='/translate')
app.register_blueprint(chat_bp, url_prefix='/chat')
app.register_blueprint(chat_vision_bp, url_prefix='/chat_vision')

# Root route
@app.route('/')
def root():
    return 'Chat Gpt API!'

if __name__ == '__main__':
    app.run(debug=True)
