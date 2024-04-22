from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

# Маршрут для генерации случайных данных
@app.route('/random_data')
def random_data():
    # Генерация случайной температуры (от -10 до 40 градусов)
    temperature = round(random.uniform(-10, 40), 1)
    
    # Генерация случайной даты (текущая дата и время)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Формирование JSON ответа
    data = {
        'temperature': temperature,
        'date': date
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
