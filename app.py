from flask import Flask
from main.routes import main_bp
import os

def create_app():
    app = Flask(
        __name__,
        static_folder="static",
        template_folder="main/templates"
    )
    app.register_blueprint(main_bp)
    return app

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))
    create_app().run(host="0.0.0.0", port=port, debug=True)
