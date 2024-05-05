from flask import Flask, jsonify
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
    
    problem = generate_problem(complexity)
    answer = solve_problem(problem)
    return problem, answer 

def get_equation():

    equation, root = generate_equation()
    return equation, root

@app.route("/send/<query>", methods=["GET"])
def index(query: list):
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
        print("kdglfgjfl")
        data = {
            "origin": equation,
            "answer": root
        }
    return jsonify(data) 

@app.route("/get_user_data/<int:id>", methods=["GET"])
def get_user_data(id):
    user = User.query.get_or_404(id)
    data = {
        "id": id, 
        "name": user.name,
        "email": user.email,
        "phone": user.phone, 
        "score_id": user.score_id,
    }
    return data

@app.route("/get_user_score_data/<int:id>", methods=["GET"])
def get_user_score_data(id):
    response = get_user_data(id)
    print(response)
    score = Score.query.get_or_404(response['score_id'])
    data = {
        "id": score.id,
        "count": score.count,
        "max": score.max,
        "min_time": score.min_time,
    }
    return data
# TODO: http://127.0.0.1:5001/get_user_data/1
# TODO: http://127.0.0.1:5001/get_user_score_data/1
# TODO: http://127.0.0.1:5001/send/[1, None]


# Реализация функции для обработки результата, она должна будет округлить и привести float в int если возможно, 
# Пример: answer = 3.(3) -> 3.3 ; 
# answer = 16.0(float) -> 16(int)