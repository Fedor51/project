from flask import Flask, jsonify, request, render_template
from config import Config
from main.models import *
from main.models.db import db
from main.services import *
from datetime import datetime
from pprint import pprint
from sqlalchemy import desc
from copy import deepcopy

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    response = request.json
    email = response["email"]
    password = response["password"]
    user = User.query.filter_by(email=email).first()

    if user == None:
        print("Login went wrong, email is invalid") ; return jsonify("0")
    
    if user.password == password:
        print("Login went successfully") ; return jsonify("1")
    
    print("Login went wrong, password is invalid") ;  return jsonify("0")

@app.route("/get/problem/<int:complexity>/<int:count>", methods=["GET"])
def get_problem(complexity, count):

    problems = [get(complexity) for i in range(count)]
    data = {
        "user_id": None,
        "questions": 
                {
                idx: {
                    "problem": pr[0],
                    "answer": pr[1], # TODO: change answers view(goal: get_problem(answers))
                    "is_correct": 0,
                    "solutions": 1 if complexity != 2 else 2
                } for idx, pr in enumerate(problems)
            } 
        }
    pprint(data)
    return jsonify(data)

@app.route("/get/user_by_email", methods=["POST"])
def get_user_by_email():
    email = request.json
    user = User.query.filter_by(email=email).first()
    tests = Test.query.filter_by(user_id=user.id).all()
    stats = get_stats(user.id).json

    data = {
        "first_name": user.first_name,
        "surname": user.surname,
        "last_name": user.last_name,
        "email": user.email,
        "password": user.password,
        "phone": user.phone,
        "tests": [ 
            {
                "id": t.id,
                "date": t.date,
                "user_id": t.user_id, 
                "questions": [{"problem": q.problem, "answer": q.answer, "is_correct": q.is_correct} for q in Question.query.filter_by(test_id=t.id).all()]
            } for t in tests
        ],
        "test_count": stats["test_count"],
        "question_count": stats["question_count"],
        "correct_rate": stats["correct_rate"],
        "correct_questions": stats["correct_questions"],
    }
    return jsonify(data)

@app.route("/get/user_id_by_email", methods=["POST"])
def get_user_id_by_email():
    email = request.json
    user = User.query.filter_by(email=email).first()
    return jsonify(user.id)

@app.route("/save_test", methods=["POST"])
def save_test():
    data = request.json

    test = Test(datetime.today().strftime("%d.%m.%Y"), data["user_id"])
    db.session.add(test)
    db.session.commit()

    for i in data["questions"]:
        q = Question(data["questions"][i]["problem"], str(data["questions"][i]["answer"]), data["questions"][i]["is_correct"], test.id)
        db.session.add(q)
        db.session.commit()
    return "0"

@app.route("/get/user/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    tests = Test.query.filter_by(user_id=id).all()

    data = {
        "first_name": user.first_name,
        "surname": user.surname,
        "last_name": user.last_name,
        "email": user.email,
        "password": user.password,
        "phone": user.phone,
        "tests": [ 
            {
                "id": t.id,
                "date": t.date,
                "user_id": t.user_id, 
                "questions": [{"problem": q.problem, "answer": q.answer, "is_correct": q.is_correct} for q in Question.query.filter_by(test_id=t.id).all()]
            } for t in tests
        ]
    }
    return jsonify(data) 

@app.route("/get/test/<int:user_id>", methods=["GET"])
def get_test(user_id):
    tests = Test.query.filter_by(user_id=user_id).all()

    data = {
       "tests": [ 
            {
                "id": t.id,
                "date": t.date,
                "user_id": t.user_id, 
                "questions": [{"problem": q.problem, "answer": q.answer, "is_correct": q.is_correct} for q in Question.query.filter_by(test_id=t.id).all()]
            } for t in tests
        ]
    }
    return jsonify(data)

@app.route("/get/all_users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    print(users)
    data = {
        "users": [
                    { 
                "first_name": user.first_name,
                "surname": user.surname,
                "last_name": user.last_name,
                "email": user.email,
                "password": user.password,
                "phone": user.phone,
                "tests": [ 
                    {
                        "id": t.id,
                        "date": t.date,
                        "user_id": t.user_id, 
                        "questions": [{"problem": q.problem, "answer": q.answer, "is_correct": q.is_correct} for q in Question.query.filter_by(test_id=t.id).all()]
                    } for t in Test.query.filter_by(user_id=user.id)
                ]
            } for user in users
        ] 
    }
    return jsonify(data)

@app.route("/get/all_tests", methods=["GET"])
def get_all_tests():
    tests = Test.query.all()
    data = {
        "tests": [
            {   
            "id": t.id,
            "date": t.date,
            "user_id": t.user_id, 
            "questions": [{"problem": q.problem, "answer": q.answer, "is_correct": q.is_correct} for q in Question.query.filter_by(test_id=t.id).all()]
            } for t in tests
        ]
    }
    return jsonify(data)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    data = request.json
    user = User(data["first_name"], data["surname"], data["last_name"], data["email"], data["password"], data["phone"])

    print("Added new user:", data)

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

    user.first_name = data["first_name"]
    user.surname = data["surname"]
    user.last_name = data["last_name"]
    user.email = data["email"]
    user.password = data["password"]
    user.phone = data["phone"]
    db.session.commit()
   
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
    test_q = Test.query.filter_by(user_id=user.id)
    
    tests = test_q.all()
    correct = 0
    all_questions = 0

    for t in tests:
        for q in  Question.query.filter_by(test_id=t.id).all():
            if q.is_correct:
                correct += 1
            all_questions += 1

    data = {
        "test_count": test_q.count(),
        "question_count": all_questions,
        "correct_rate": f"{round((correct / all_questions) * 100, 2)}" if all_questions != 0 else "0",
        "correct_questions": correct
    }
    return jsonify(data)
# rating 
@app.route("/get/rating", methods=['GET'])
def get_rating():
    # qry = session.query(Data).filter(Data.user_id == user_id).order_by(desc(Data.counter).limit(1)    
    data = {
        "users":[
                get_stats(i+1).json for i in range(User.query.count())
        ]
    }
    max_test_count = sorted(data["users"], key=lambda d: d['test_count'], reverse=True)[0]
    max_question_count = sorted(data["users"], key=lambda d: d['question_count'], reverse=True)[0]

    data1 = deepcopy(data)
    data1["users"].remove(max_test_count)
    for i in data1["users"]:
        if i["test_count"] == max_test_count["test_count"]:
            max_test_count = "0"
            break

    data["users"].remove(max_question_count)
    for i in data["users"]:
        if i["question_count"] == max_question_count["question_count"]:
            max_question_count = "0"
            break
    d = {   
        "max_test_count": max_test_count, # "0" if it does not seem to have leader  
        "max_question_count": max_question_count,
    }
    pprint(d)
    return jsonify(d)


# 0^0 = 1  python logic!!!