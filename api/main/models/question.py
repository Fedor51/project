from .db import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    problem = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    is_correct = db.Column(db.Integer, nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey("test.id"), nullable=False)

    # tests = db.relationship("Test", back_populates="questions")
    
    def __init__(self, problem, answer, is_correct, test_id) -> None:
        self.problem = problem
        self.answer = answer
        self.is_correct = is_correct
        self.test_id = test_id