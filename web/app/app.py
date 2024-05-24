from flask import Flask, render_template, redirect, url_for, request, jsonify,session
import requests

app = Flask(__name__)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]0/'

colOfPrim = 6
answers=0

# Главная страница с кнопкой
@app.route('/')
def index():
    if 'username' not in session:
        return render_template('login.html')
    return render_template('index.html')

@app.route('/accaunt',methods=['POST','GET'])
def accaunt():
    if request.method=='POST':
        newData={
            'newName':request.form['newname'],
            'newPassword':request.form['newpassword'],
            'mail':request.form['mail']+'@'+request.form['mailmail']
        }
        return redirect('/'), jsonify(newData)
    username='имя'
    password='пароль'
    mail='mail@mail.com'
    primResh=21      #затычки
    mailmail='mail.com'
    nmail=mail.replace('@'+mailmail,'')
    prist=primResh//100
    grad=primResh%100
    return render_template('accaunt.html', name=username,password=password,primResh=primResh,grad=grad,prist=prist,mail=nmail,mailmail=mailmail)

@app.route('/logun', methods=['POST','GET'])
def logun():
    username=request.form['username']
    password=request.form['password']
    data={
        'email':username,
        'password':password
    }
    response = requests.post("http://127.0.0.1:5001/login", json=data)
    
    if response == '0':
        return redirect(url_for('login'))

    session['username'] = username
    return redirect(url_for('index'))

@app.route('/logout') 
def logout(): 
    # Удаляем имя пользователя из сессии при выходе
    session.pop('username', None) 
    return render_template('login.html')

@app.route('/YGT')
def answer():
    api_url = 'http://127.0.0.1:5000/primdata'
    response = requests.get(api_url)
    return render_template('answer.html',goodAnswers=response.json()['answers'])


# Страница для отображения данных
@app.route('/display_answer',methods=["GET",'POST'])
def display():
    if request.form == "GET":
        choice = request.form["Level"]
        compexity = int(choice)
        count = 5
        data = requests.get(f'http://127.0.0.1:5001/get/problem/{compexity}/{count}')
        return render_template("display.html", data=data)
    
    # ###
    answer = request.form["YourAnswer"]
    if answer == data["answer"]:

        print(answer)

    return render_template('display.html',Prim=truePrim,znaki=znaki,numsInPrim=numsInPrim,colOfPrim=colOfPrim,truePrim=truePrim)


@app.route('/log/<username>/<password>')
def log(username, password):
    api_url = 'http://127.0.0.1:5000/data'
    response = requests.get(api_url)
    
    data = response.json()
    
    if username in data['users'] and password == data['passwords'][data['users'].index(username)]:
        session['username'] = username
        return redirect(url_for('index'))
    return redirect(url_for('logun'))


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        
        login = request.form['login']

        firstName=request.form['firstName']
        surname=request.form['surname']
        lastName=request.form['lastName']

        password = request.form['password']
        
        mail = request.form['mail']
        phone = request.form['phoneNumber']

        data={
        'login':login,
        'firstname':firstName,
        'surname':surname,
        'lastName':lastName,
        'password':password,
        'email':mail,
        'phoneNumber':phone
        }
        session['username'] = mail


        requests.post("http://127.0.0.1:5001/add_user", json=data)

        return redirect(url_for('index'))
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
