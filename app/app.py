from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

# Главная страница с кнопкой
@app.route('/')
def index():
    return render_template('index.html')

# Обработчик для кнопки получения данных
@app.route('/get_data')
def get_data():
    # URL второго API, который мы будем вызывать
    api_url = 'http://127.0.0.1:5001/random_data'
    
    # Отправляем GET запрос к другому API
    response = requests.get(api_url)
    
    # Получаем JSON данные
    data = response.json()
    
    # Перенаправляем на другую страницу и передаем данные в URL
    return redirect(url_for('display_data', temperature=data['temperature'], date=data['date']))

# Страница для отображения данных
@app.route('/display_data/<float:temperature>/<date>')
def display_data(temperature, date):
    return render_template('display.html', temperature=temperature, date=date)

if __name__ == '__main__':
    app.run(debug=True)
