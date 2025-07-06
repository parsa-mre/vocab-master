from .. import db
from sqlalchemy.dialects.postgresql import ARRAY


class Word(db.Model):
    __tablename__ = "words"
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text, nullable=False)
    part_of_speech = db.Column(db.Text, nullable=False)
    gender = db.Column(db.Text, nullable=True)
    translation = db.Column(db.Text, nullable=False)
    examples = db.Column(ARRAY(db.Text), nullable=True)
