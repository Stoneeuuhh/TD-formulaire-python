from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/afficher/", methods=["GET", "POST"])
def afficher():

    if request.method == "POST":
        nom = request.form.get("nom")
        mail = request.form.get("mail")
        message = request.form.get("message")

    else:
        nom = request.args.get("nom")
        mail = request.args.get("mail")
        message = request.args.get("message")

    return render_template(
        "reponse.html",
        nom=nom,
        mail=mail,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
