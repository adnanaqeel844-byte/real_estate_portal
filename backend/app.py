from flask import Flask
from flask_cors import CORS
from config import Config
from database import db
from routes.auth import auth_bp
from routes.admin import admin_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
