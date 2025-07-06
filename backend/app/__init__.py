from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize SQLAlchemy (no app yet)
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Register blueprints
    from app.routes.health import health_bp

    app.register_blueprint(health_bp)

    return app


# Create the Flask app
app = create_app()


@app.route("/")
def hello():
    return "Hello, World!"


# Optional: CLI command to create tables
def create_tables():
    with app.app_context():
        db.create_all()
        print("Tables created.")


if __name__ == "__main__":
    # Uncomment the next line to create tables on startup (for dev only)
    # create_tables()
    app.run(host="0.0.0.0", port=2323, debug=True)
