from flask import Flask
from main.routes import main_bp

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="main/templates")
    app.register_blueprint(main_bp)
    return app

if __name__ == "__main__":
    create_app().run(debug=True)
