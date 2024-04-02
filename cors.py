from flask_cors import CORS

def configure_cors(app):
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
