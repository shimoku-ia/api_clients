py -3 -m venv .venv
.venv\scripts\activate

python -m pip install


python -m flask run 

pip3 freeze>requirements.txt

export FLASK_APP = application.py
export FLASK_ENV = development


python

from enum import unique
from tkinter.tix import INTEGER
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db=SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    description=db.Column(db.String(120))
    def __repr__(self):
        return f"{self.name}- {self.description}"



@app.route("/")
def index():
    return "Hello, Shimokins IA SUPERS!"

@app.route("/drinks")
def get_drinks():
    return {"drinks":"drinks soda"}

@app.route('/drinks/<id>')
def get_drink(id):
    return ({"name":"kola-kala"})

@app.route("/drinks",method=['POST'])
def add_drink():
    return({'id':'sdfsfsfs'})

@app.route("/drinks/<id>",method=['DELETE'])
def delete_drink():
    if notfuoud:
        return {"error":"not found this drink",'drink':id}
    return {'good':'removes'}
