#Created by Github.com/JoaoKrapp
#test
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from main import *

app = Flask(__name__)
app.secret_key = "segredo"
app.permanent_session_lifetime = timedelta(seconds=5)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        sudoku= [
            [int(request.form["c1"]), int(request.form["c2"]), int(request.form["c3"]), int(request.form["c4"]), int(request.form["c5"]), int(request.form["c6"]), int(request.form["c7"]), int(request.form["c8"]), int(request.form["c9"])],
            [int(request.form["c10"]), int(request.form["c11"]), int(request.form["c12"]), int(request.form["c13"]), int(request.form["c14"]), int(request.form["c15"]), int(request.form["c16"]), int(request.form["c17"]), int(request.form["c18"])],
            [int(request.form["c19"]), int(request.form["c20"]), int(request.form["c21"]), int(request.form["c22"]), int(request.form["c23"]), int(request.form["c24"]), int(request.form["c25"]), int(request.form["c26"]), int(request.form["c27"])],
            [int(request.form["c28"]), int(request.form["c29"]), int(request.form["c30"]), int(request.form["c31"]), int(request.form["c32"]), int(request.form["c33"]), int(request.form["c34"]), int(request.form["c35"]), int(request.form["c36"])],
            [int(request.form["c37"]), int(request.form["c38"]), int(request.form["c39"]), int(request.form["c40"]), int(request.form["c41"]), int(request.form["c42"]), int(request.form["c43"]), int(request.form["c44"]), int(request.form["c45"])],
            [int(request.form["c46"]), int(request.form["c47"]), int(request.form["c48"]), int(request.form["c49"]), int(request.form["c50"]), int(request.form["c51"]), int(request.form["c52"]), int(request.form["c53"]), int(request.form["c54"])],
            [int(request.form["c55"]), int(request.form["c56"]), int(request.form["c57"]), int(request.form["c58"]), int(request.form["c59"]), int(request.form["c60"]), int(request.form["c61"]), int(request.form["c62"]), int(request.form["c63"])],
            [int(request.form["c64"]), int(request.form["c65"]), int(request.form["c66"]), int(request.form["c67"]), int(request.form["c68"]), int(request.form["c69"]), int(request.form["c70"]), int(request.form["c71"]), int(request.form["c72"])],
            [int(request.form["c73"]), int(request.form["c74"]), int(request.form["c75"]), int(request.form["c76"]), int(request.form["c77"]), int(request.form["c78"]), int(request.form["c79"]), int(request.form["c80"]), int(request.form["c81"])]
        ]
        session.permanent = True
        solve_sudoku(sudoku)
        session["sudoku"] = sudoku

        return redirect(url_for("solved"))
    else:
        return render_template("index.html")

@app.route("/solved", methods=["POST", "GET"])
def solved():
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("solved.html")

if __name__ == "__main__":
    app.run(debug=True)