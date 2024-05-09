from .db import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
    users = db.relationship("User", back_populates="tests")

    def __init__(self, count, time, user_id) -> None:   
        self.count = count
        self.time = time
        self.user_id = user_id