from flask import Flask, jsonify
from api.services.generate import *

app = Flask(__name__)


def generate_problem(complexity: bool):
    # complexity is False(easy) or True(middle)
    if complexity:
        return math_gen_complexity_easy()
    else:
        return math_gen_complexity_middle(eq=False)

def generate_equation():
    return math_gen_complexity_middle(eq=True)



def get_problem(complexity: bool):
    
    problem = generate_problem(complexity)
    answer = solve_problem(problem)
    return problem, answer 

def get_equation():

    equation = generate_equation()
    root = solve_eq(equation)
    return equation, root

@app.route("/send/<query>", methods=["GET"])
def index(query: list):
    # query[0] is 0(problem), 1(equation)
    # query[1] is problem complexity False or True (None if query[0] is 1)
    
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
    return data 

    # data = {
    #     "id": id,
    #     "origin": problem,
    #     "answer" : answer, 
    # }
    
    # return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
