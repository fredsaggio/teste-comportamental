from flask import Flask, render_template, request, flash, redirect
from models import pergunta_class

app = Flask(__name__)
app.config["SECRET_KEY"] = "<senha-secreta>"

from views import *

if __name__ == "__main__":
    app.run(debug=True)