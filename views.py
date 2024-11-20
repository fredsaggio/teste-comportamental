from main import app
from flask import render_template

@app.route("/")
def home():
    return render_template("inicio.html")

@app.route('/perguntas')
def destino():
    return render_template('perguntas1.html')