from flask import Flask, render_template, redirect, url_for, request, flash


app = Flask(__name__)
app.secret_key = "supersecretkey"  


import sqlite3
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"


   

def get_reponses(methode):

    

@app.route("/")
def index():
    """Redirige vers la première question du quiz."""
    return redirect(index.html)

@app.route("/afficher/")
def afficher(nom, mail, message):
    return render_template("reponse.html", nom=nom, question=request.args.get('question'), reponse=request.args.get('reponse'))


if __name__ == "__main__":
    app.run(debug=True)