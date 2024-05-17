from .db import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    data = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
    
    users = db.relationship("User", back_populates="tests")
    # questions = db.relationship("Question", back_populates="tests")
    
    def __init__(self, date, user_id) -> None:   
        self.date = date
        self.user_id = user_id