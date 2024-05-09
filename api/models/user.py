from .db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    tests = db.relationship("Test", back_populates="users")

    def __init__(self, name, email, phone, password) -> None:
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password 