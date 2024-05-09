from flask import Flask, jsonify, request
from config import Config
from api.services.generate import *
from api.models import *
from api.models.db import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


def generate_problem(complexity: int):
    # complexity is False(easy) or True(middle)
    if complexity:
        return math_gen_complexity0()
    else:
        return math_gen_complexity2()

def generate_equation():
    return math_gen_equation0()

def get_problem(complexity: int):
    
    problem, answer = generate_problem(complexity)
    return problem, answer 

def get_equation():

    equation, root = generate_equation()
    return equation, root

@app.route("/get_problem/<query>", methods=["GET"])
def get(query: list):
    # query[0] is 0(problem), 1(equation)
    # query[1] is problem complexity: 0 or 1 (None if query[0] is 1)
    
    if not query[0]:
        problem, answer = get_problem(query[1])
        data = {
            "origin": problem, 
            "answer": answer
        }
    else:
        equation, root = get_equation() 
       
        data = {
            "origin": equation,
            "answer": root
        }
    return jsonify(data) 

@app.route("/get/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    tests = Test.query.filter_by(user_id=id).all()

    data = {
        "id": id, 
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "phone": user.phone,
        "tests": [{"id": t.id, "count": t.count, "time": t.time, "user_id": t.user_id} for t in tests]
    }

    return jsonify(data)

@app.route("/get/test/<int:user_id>", methods=["GET"])
def get_test(user_id):
    tests = Test.query.filter_by(user_id=user_id).all()

    data = {
       "tests": [{"id": t.id, "count": t.count, "time": t.time, "user_id": t.user_id} for t in tests]
    }
    return jsonify(data)

@app.route("/get/all_users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    data = [{
        "id": user.id,
        "name": user.name, 
        "email": user.email, 
        "password": user.password, 
        "phone": user.phone,
        "tests": [{"id": t.id, "count": t.count, "time": t.time, "user_id": t.user_id} for t in Test.query.filter_by(user_id=user.id).all()]
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
        } for test in tests ]
    
    return jsonify(data)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():

    data = request.json
    user = User(data["name"], data["email"], data["phone"], data["password"])

    print(data)

    db.session.add(user)
    db.session.commit()

    return "New user added successfully"

@app.route("/add_test", methods=["GET", "POST"])
def add_test():
    
    data = request.json
    test = Test(data["count"], data["time"], data["user_id"])

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


# Реализация функции для обработки результата, она должна будет округлить и привести float в int если возможно, 
# Пример: answer = 3.(3) -> 3.3 ; 
# answer = 16.0(float) -> 16(int)
