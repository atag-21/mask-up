from flask import Flask, request, render_template
from markupsafe import Markup
from urllib.request import  urlopen

from detect import ismasked as im

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/entry", methods=["POST", "GET"])
def entry():
    MESSAGE = ""
    if request.method == "GET":
        return render_template("entry.html")

    elif request.method == "POST":
        min_balance = 12
        balance = float(request.form.get("balance").strip())
        if balance >= min_balance:
            MESSAGE = MESSAGE + "✔ You have enough balance <br>"
            balance_is_enough = True
        else:
            MESSAGE = MESSAGE + "❌ You do NOT have enough balance <br>"
            balance_is_enough = False

        imgb64 = request.form.get("b64p")
        with urlopen(imgb64) as b64img:
            img = b64img.read()
            with open("image.png", "wb") as f:
                f.write(img)
        maskedup = im("image.png") # Determine if user is masked-up!

        if maskedup == True:
            MESSAGE = MESSAGE + "✔ You are wearing a mask <br>"
        else:
            MESSAGE = MESSAGE + "❌ You are NOT wearing a mask <br>"

        if maskedup and balance_is_enough:
            MESSAGE = MESSAGE + "✔ You may pass!"
        else:
            MESSAGE = MESSAGE + "❌ You may NOT pass!"
        STATUS = "to_be_computed"
        MESSAGE = Markup(MESSAGE)
        return render_template("response.html", status = STATUS, message = MESSAGE)