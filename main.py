# encoding: utf-8
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "<senha-secreta>"

from views import *

if __name__ == "__main__":
    app.run(debug=True)