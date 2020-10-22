from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from base import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://das:das@localhost/bustomoviles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# engine = create_engine('')

# db = SQLAlchemy(app)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    usuario = Column(String(20), unique=True)
    email = Column(String(30), unique=True)
    passwd = Column(String(80))

    def __init__(self, usuario, email, passwd):
        self.usuario = usuario
        self.email = email
        self.passwd = passwd


class Marca(Base):
    __tablename__ = 'marca'
    id = Column(Integer, primary_key=True)
    marca = Column(String(20), unique=True)
    pais = Column(String(20))

    def __init__(self, marca, pais):
        self.marca = marca
        self.pais = pais


class Coche(Base):
    __tablename__ = 'coche'
    id = Column(Integer, primary_key=True)
    marca = Column(Integer, ForeignKey('marca.id'))
    modelo = Column(String(30))
    anyo = Column(Integer)
    kilometros = Column(Integer)
    combustible = Column(String)
    potencia = Column(Integer)
    descripcion = Column(String)
    precio = Column(Integer)
    img = Column(String)

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

