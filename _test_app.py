## send data on main application(http://127.0.0.1:5001/add_user)

import requests

url = "http://127.0.0.1:5001/login"


def index():
    data = {
        "email": "email1",
        "password": "password12",
    }

    print(data)
    requests.post(url, json=data) #.__dict__
    print("Posted successfully")
    return "Posted successfully"

if __name__ == '__main__':
    index()