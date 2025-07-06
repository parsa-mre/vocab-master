from flask import Blueprint, jsonify
from flask import request
from openai import OpenAI
from pydantic import BaseModel
import json
import os


class WordListExtractionRequest(BaseModel):
    words: list[str]


# Text processing blueprint
parse_bp = Blueprint("parse", __name__)


@parse_bp.route("/parse", methods=["POST"])
def parse_text():
    """
    Parse text endpoint
    Accepts JSON with a 'text' field and returns a placeholder response.
    """

    data = request.get_json()
    text = data.get("text", "") if data else ""

    client = OpenAI()

    r = client.responses.create(
        prompt={
            "id": os.getenv("OPENAI_EXTRACTION_PROMPT_ID"),
            "version": os.getenv("OPENAI_PROMPT_VERSION"),
        },
        input=text,
        model=os.getenv("OPENAI_MODEL"),
    )

    print(r)

    response_text = json.loads(r.output[0].content[0].text)

    return jsonify(
        {
            "message": response_text,
            "status": "not implemented yet",
            "received_text": text,
        }
    )
