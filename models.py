from base import Base
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class Coche(Base):
    __tablename__ = 'coche'
    id = Column(Integer, primary_key=True)
    marca_id = Column(Integer, ForeignKey('marca.id'))
    marca = relationship("Marca", back_populates="coches")
    modelo = Column(String(30))
    anyo = Column(Integer)
    kilometros = Column(Integer)
    combustible = Column(String)
    potencia = Column(Integer)
    descripcion = Column(String)
    precio = Column(Integer)
    ciudad = Column(String)
    img = Column(String)

    def __init__(self, marca, modelo, anyo, kilometros, combustible, potencia, descripcion, precio, ciudad, img):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.kilometros = kilometros
        self.combustible = combustible
        self.potencia = potencia
        self.descripcion = descripcion
        self.precio = precio
        self.ciudad = ciudad
        self.img = img

class User(Base, UserMixin):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)

users = []
def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None

class Marca(Base):
    __tablename__ = 'marca'
    id = Column(Integer, primary_key=True)
    marca = Column(String(20), unique=True)
    pais = Column(String(20))
    coches = relationship("Coche")

    def __init__(self, marca, pais):
        self.marca = marca
        self.pais = pais