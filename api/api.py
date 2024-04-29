from flask import Flask, jsonify
import random

app = Flask(__name__)

# Маршрут для генерации случайных данных
@app.route('/random_problem')
def random_problem():
    numbers_count = random.randint(2, 10)
    problem = [str(random.randint(0, 20)) for num in range(numbers_count)]
    operators = ['+', '-', '*', "/"]

    for i in range(1, len(problem)*2 - 1, 2):
        problem.insert(i, random.choice(operators))
    problem = "".join(problem)
    
    answer = eval(problem)

    id = random.randint(0, 100)

    data = {
        "id": id,
        "problem": problem,
        "answer" : answer, 
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
