from flask import Flask, render_template, redirect, url_for, request, jsonify,session
from random import randint, choice
import string
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
    return redirect(url_for('log',username=username,password=password))


@app.route('/submit', methods=['POST'])
def submit():
    choice = request.form['Level']
    #print(f'Выбран вариант: {choice}')
    znaks=['+','-','*','÷','^']
    if choice=='hardLevel':
        numsInPrim = randint(3,16)
    elif choice=="normalLevel":
        znaks.pop()
        numsInPrim = randint(3,11)
    else:
        znaks=znaks[:-3]
        numsInPrim = randint(3,5)
    znaks=''.join(znaks)
    return redirect(url_for(".display",numsInPrim=numsInPrim,znaki=znaks,answers=0,colOfPrim=6,truePrim='None')) #colOfPrim-затычка


@app.route('/YGT')
def answer():
    api_url = 'http://127.0.0.1:5000/primdata'
    response = requests.get(api_url)
    return render_template('answer.html',goodAnswers=response.json()['answers'])


# Страница для отображения данных
@app.route('/trueDisplay/<numsInPrim>/<znaki>/<colOfPrim>/<truePrim>',methods=["GET",'POST'])
def display(numsInPrim,znaki,colOfPrim,truePrim):
    colOfPrim=int(colOfPrim)
    global answers
    if colOfPrim<=0:
        primData()
        return redirect(url_for('.answer'))
    
    
    if request.method=='POST' and colOfPrim!=6:
        answer=int(custom_eval(truePrim))
        userA=request.form['YourAnswer']
        
        if userA != '' and userA not in list(string.ascii_letters):
            userA=int(userA)
            if answer==userA:
                answers+=1
        else:
            redirect(url_for('.BRUH',numsInPrim=numsInPrim,znaki=znaki,colOfPrim=colOfPrim))
    znaki=normilizer(list(znaki))
    numsInPrim=int(numsInPrim)    
    colOfPrim-=1   
    prim=list()
    for i in range(1,numsInPrim+1,2):
        prim.append(str(randint(1,100)))
        prim.append(choice(znaki))
        if prim[-1]=="^":
            prim.append(str(randint(1,3)))
            prim.append(choice(znaki[:-1]))
    prim.pop(-1)
    truePrim="".join(prim)

    answer=int(custom_eval(truePrim))
    
    return render_template('display.html',Prim=truePrim,znaki=znaki,numsInPrim=numsInPrim,colOfPrim=colOfPrim,truePrim=truePrim)


@app.route('/primdata')
def primData():

    primData={
        'answers':answers
    }
    return jsonify(primData)

def normilizer(foo):
    valid_operators = {'+', '-', '*', '÷', '^'}
    result = [x for x in foo if x in valid_operators]
    return result



def finderOfIndex(baz,foo):
    if baz in foo:
        return foo.index(baz)
    else:
        return None

def custom_eval(expression):
    mapping = {
        '÷': '/',
        '^': '**' 

    }
    
    # Замена символов с помощью map
    for key, value in mapping.items():
        expression = expression.replace(key, value)
    
    # Выполнение выражения после замены
    result = eval(expression)
    return result


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
        
        username=request.form['firstName']
        password = request.form['password']
        mail = request.form['mail']
        data={
        'name':username,
        'password':password,
        'email':mail,
        'phone':0
        }
        session['username'] = username


        requests.post("http://127.0.0.1:5001/add_user", json=data)

        return redirect(url_for('index'))
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)

