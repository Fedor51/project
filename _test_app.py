## send data on main application(http://127.0.0.1:5001/add_user)

import requests

url = "http://127.0.0.1:5001/add_user"


def index():
    data = {
        "name": "TEST111",
        "email": "TEST@example.com1111",
        "phone": "+7(xxx)-xxx-xx-xx1111",
        "password": "TEST11111",
    }
    # data = {
    #     "count": 1000,
    #     "time": "xx:xx:xxx",
    #     "user_id": 1
    # }
    print(data)
    requests.post(url, json=data) #.__dict__
    print("Posted successfully")
    return "Posted successfully"

if __name__ == '__main__':
    index()
