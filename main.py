from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import create_engine, Column, String, Integer
from base import base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://das:das@localhost/bustomoviles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('mysql://root:root@localhost/bustomoviles')

# db = SQLAlchemy(app)

class User(Base):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), unique=True)
    passwd = db.Column(db.String(80))

    def __init__(self, usuario, email, passwd):
        self.usuario = usuario
        self.email = email
        self.passwd = passwd


class Marca(db.Model):
    __tablename__ = 'marca'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(20), unique=True)
    pais = db.Column(db.String(20))

    def __init__(self, marca, pais):
        self.marca = marca
        self.pais = pais


class Coche(db.Model):
    __tablename__ = 'coche'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.relationship('marca')
    modelo = db.Column(db.String(30))
    anyo = db.Column(db.Integer)
    kilometros = db.Column(db.Integer)
    combustible = db.Column(db.String)
    potencia = db.Column(db.Integer)
    descripcion = db.Column(db.String)
    precio = db.Column(db.Integer)
    img = db.Column(db.String)

    def __init__(self, marca, modelo, anyo, kilometros, combustible, potencia, descripcion, precio, img):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.kilometros = kilometros
        self.combustible = combustible
        self.potencia = potencia
        self.descripcion = descripcion
        self.precio = precio
        self.img = img

