from flask import Flask, render_template, redirect, url_for, request, session
import requests

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]0/'



@app.route("/")
def index():
    if "email" not in session:
        return render_template("login.html")
    return render_template("index.html")


@app.route("/account", methods=["POST", "GET"])
def account():
    email = session["email"]
    data = requests.post("http://127.0.0.1:5001/get/user_by_email", json=email).json()
    return render_template("account.html", data=data)


@app.route("/login", methods=["POST", "GET"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    data = {"email": email, "password": password}
    response = requests.post("http://127.0.0.1:5001/login", json=data).json()
    if response == "0":
        return render_template("login.html")
    session["email"] = email
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.pop("email")
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/rating")
def rating():
    resp = requests.get("http://127.0.0.1:5001/get/rating").json()
    return render_template("rating.html", data=resp['users'])

@app.route("/display/<ac>/<int:complexity>", methods=["GET", "POST"])
def display(ac, complexity):
    if ac == "get":
        option = request.form["level"]
        complexity = int(option)
        count = 5
        global data
        data = requests.get(
            f"http://127.0.0.1:5001/get/problem/{complexity}/{count}"
        ).json()
        return render_template("display.html", data=data, complexity=complexity)

    if complexity == 2:
        answers = [[request.form[f"{i}"], request.form[f"{i}i"]] for i in range(5)]
        for idx, answer in enumerate(answers):
            if (
                answer[0].replace(" ", "") in data["questions"][f"{idx}"]["answer"]
                and answer[1].replace(" ", "") in data["questions"][f"{idx}"]["answer"]
            ):
                data["questions"][f"{idx}"]["is_correct"] = 1

    else:
        answers = [request.form[f"{i}"] for i in range(5)]
        for idx, answer in enumerate(answers):
            if answer == data["questions"][f"{idx}"]["answer"]:
                data["questions"][f"{idx}"]["is_correct"] = 1

    data["user_id"] = requests.post(
        "http://127.0.0.1:5001/get/user_id_by_email", json=session["email"]
    ).json()
    requests.post("http://127.0.0.1:5001/save_test", json=data)

    return render_template(
        "answer.html", data=data, answers=answers, complexity=complexity
    )


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":

        first_name = request.form["first_name"]
        surname = request.form["surname"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        email = request.form["email"]
        phone = request.form["phone"]

        data = {
            "first_name": first_name,
            "surname": surname,
            "last_name": last_name,
            "password": password,
            "email": email,
            "phone": phone,
        }
        session["email"] = email
        requests.post("http://127.0.0.1:5001/add_user", json=data)
        return redirect(url_for("index"))

    return render_template("signup.html")

@app.route("/drop_user")
def drop_user():
    id = requests.post("http://127.0.0.1:5001/get/user_id_by_email", json=session['email']).json()
   
    requests.get(f"http://127.0.0.1:5001/drop_user/{id}")
    session.pop("email")
    return redirect(url_for("index"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        data = {
            "first_name": request.form["first_name"],
            "surname": request.form["surname"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "phone": request.form["phone"],
            "password": request.form["password"],
        }
        id = requests.post(
            "http://127.0.0.1:5001/get/user_id_by_email", json=session["email"]
        ).json()
        requests.post(f"http://127.0.0.1:5001/edit_user/{id}", json=data)
        return redirect(url_for("account"))

    resp = requests.post(
        "http://127.0.0.1:5001/get/user_by_email", json=session["email"]
    ).json()
    return render_template("edit.html", data=resp)


if __name__ == "__main__":
    app.run(debug=True)
