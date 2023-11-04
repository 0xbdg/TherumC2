from flask import *
import sys

setup = Flask(__name__, template_folder="template")

@setup.route('/', methods=["GET","POST"])
def log():
    if (request.method == "POST"):
        pass
    else:
        return render_template("login.html")

@setup.route("/panel")
def panel():
    return render_template("panel.html")

if (__name__ == "__main__"):
    setup.run(debug=True, host="localhost", port=8080)
