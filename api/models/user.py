from .db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    score_id = db.Column(db.Integer, db.ForeignKey('score.id'), nullable=False)
    
    def __init__(self, name, email, phone, score_id) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.score_id = score_id