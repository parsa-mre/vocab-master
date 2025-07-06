from flask import Blueprint, jsonify

# Create the main API blueprint
api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

# Import and register all route modules
from . import parse

# Register sub-blueprints
api_bp.register_blueprint(parse.parse_bp)


@api_bp.route("/")
def api_info():
    """
    API information endpoint
    Returns basic API information and available endpoints
    """
    return jsonify(
        {
            "name": "Vocab Master API",
            "version": "v1",
            "status": "active",
            "endpoints": {
                "parse": "/api/v1/parse",
                "flashcards": "/api/v1/flashcards",
                "definitions": "/api/v1/definitions",
            },
        }
    )
