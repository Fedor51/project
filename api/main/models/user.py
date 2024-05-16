from .db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    tests = db.relationship("Test", back_populates="users")

    def __init__(self, first_name, surname, last_name, email, password, phone) -> None:
        self.first_name = first_name
        self.surname = surname
        self.last_name = last_name
        self.email = email
        self.password = password 
        self.phone = phone