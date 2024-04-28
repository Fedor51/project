from flask import *
import requests

app = Flask(__name__)

# Главная страница с кнопкой
@app.route('/')
def index():
    return render_template('index.html')

# Обработчик для кнопки получения данных
@app.route('/get_random_problem')
def get_problem():
    # URL второго API, который мы будем вызывать
    api_url = 'http://127.0.0.1:5001/random_problem'
    
    # Отправляем GET запрос к другому API
    response = requests.get(api_url)
    
    # Получаем JSON данные
    data = response.json()
    
    # Перенаправляем на другую страницу и передаем данные в URL
    return render_template('display.html', id=data["id"], problem=data["problem"], answer=data["answer"])

@app.route("/display_answer/<int:id>", methods=["GET", "POST"])
def display_answer(id, answer):
    u_answer = request.form["answer"] 
    return render_template("answer.html", answer=answer, u_answer=u_answer)

# Страница для отображения данных
# @app.route('/display_data/<int:id>')
# def display_data(id, problem):
#     return render_template("display.html", id=id, problem=problem)

if __name__ == '__main__':
    app.run(debug=True)
