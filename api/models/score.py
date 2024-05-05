from .db import db

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    count = db.Column(db.Integer)
    max = db.Column(db.Integer)
    min_time = db.Column(db.String)

    def __init__(self, count, max, min_time) -> None:
        self.count = count
        self.max = max
        self.min_time = min_time 