from flask import Flask, jsonify, request
from config import Config
from main.models import *
from main.models.db import db
from main.services import *

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    response = request.json
    email = response["email"]
    password = response["password"]
    user = User.query.filter_by(email=email).first_or_404()
    if user.password == password:
        print("Login went successfully") ; return "1"
    print("Login went wrong, email or password is invalid") ;  return "0"

@app.route("/get_problem/<int:complexity>", methods=["GET"])
def get_problem(complexity):
    resp = get(complexity)
    data = {
        "problem": resp[0],
        "answer": resp[1]
    }
    return jsonify(data)

@app.route("/get/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    tests = Test.query.filter_by(user_id=id).all()

    data = {
        "id": id, 
        "first_name": user.first_name,
        "surname": user.surname,
        "last_name": user.last_name,
        "email": user.email, 
        "password": user.password,
        "phone": user.phone,
        "tests": [{"id": t.id, "date": t.date, "user_id": t.user_id} for t in tests]
    }

    return jsonify(data)

@app.route("/get/test/<int:user_id>", methods=["GET"])
def get_test(user_id):
    tests = Test.query.filter_by(user_id=user_id).all()

    data = {
       "tests": [{"id": t.id, "date": t.date, "user_id": t.user_id} for t in tests]
    }
    return jsonify(data)

@app.route("/get/all_users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    data = [{
        "id": user.id,
        "first_name": user.first_name, 
        "surname": user.surname, 
        "last_name": user.last_name, 
        "email": user.email, 
        "password": user.password, 
        "phone": user.phone,
        "tests": [{"id": t.id, "date": t.date, "user_id": t.user_id} for t in Test.query.filter_by(user_id=user.id).all()]
        } for user in users ]
    return jsonify(data)

@app.route("/get/all_tests", methods=["GET"])
def get_all_tests():
    tests = Test.query.all()
    data = [{
        "id": test.id,
        "count": test.count, 
        "time": test.time, 
        "user_id": test.user_id, 
        "correct": test.correct
        } for test in tests ]
    
    return jsonify(data)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    data = request.json
    user = User(data["first_name"], data["surname"], data["last_name"], data["email"], data["password"], data["phone"])

    print(data)

    db.session.add(user)
    db.session.commit()

    return "New user added successfully"

@app.route("/add_test", methods=["GET", "POST"])
def add_test():
    
    data = request.json
    test = Test(data["date"], data["user_id"])

    print(data, test)

    db.session.add(test)
    db.session.commit()

    return "New test added successfully"  

@app.route("/edit_user/<int:id>", methods=["GET", "POST"])
def edit_user(id):
    
    data = request.json
    user = User.query.filter_by(id=id).first_or_404()

    user.name = data["name"]
    user.email = data["email"]
    user.phone = data["phone"]
    user.password = data["password"]
    db.session.commit()
    print("User updated successfully")
    return "User updated successfully"

@app.route("/drop_user/<int:id>", methods=["GET"])
def drop_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()

    return "User deleted successfully"

@app.route("/drop_test/<int:id>", methods=["GET"])
def drop_test(id):
    test = Test.query.get_or_404(id)
    db.session.delete(test)
    db.session.commit()

    return "Test deleted successfully"

# stats
@app.route("/get/stats/<int:id>", methods=['GET'])
def get_stats(id):
    user = User.query.get_or_404(id)
    tests = Test.query.filter_by(user_id=id).all()
    total = sum(t.count for t in tests)
    total_correct = sum(t.correct for t in tests)
    data = {
        "name" : user.name,
        "tests": [{"id": t.id, "count": t.count, "time": t.time, "user_id": t.user_id, "correct": t.correct} for t in tests],
        "total" : total,
        "total_correct" : total_correct,
        "correct_rate":  f"{round((total_correct / total) * 100, 2)}%" if total != 0 else "0.0%"
    }
    return jsonify(data)

# rating 
@app.route("/get/rating", methods=['GET'])
def get_rating():
    # users = User.query.order_by(User.test.count)
    # data = [{
    #     "id": id, 
    #     "name": user.name,
    #     "email": user.email,
    #     "password": user.password,
    #     "phone": user.phone,
    # } for user in users]

    # return jsonify(data)
    pass


# 0^0 = 1  python logic!!!