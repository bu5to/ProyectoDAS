from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, select, func
from sqlalchemy.orm import relationship
from base import Base, Session
from coche import Coche
from marca import Marca
from usuario import Usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/bustomoviles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# session.query(MyTable.col1).count()


@app.route('/')
def hello_world():
    session = Session()
    query = session.query(Coche)
    query = query.filter(Coche.ciudad == "Donostia")
    query = query.with_entities(func.count())
    nCochesdonos = query.scalar()
    query = session.query(Coche)
    query = query.filter(Coche.ciudad == "Bilbao")
    query = query.with_entities(func.count())
    nCochesbilbo = query.scalar()
    query = session.query(Coche)
    query = query.filter(Coche.ciudad == "Vitoria")
    query = query.with_entities(func.count())
    nCochesvito = query.scalar()
    query = session.query(Coche)
    coches = query.all()
    query = session.query(Marca)
    marcas = query.all()
    query = session.query(Coche.ciudad.distinct().label("ciudad"))
    ciudades = [row.ciudad for row in query.all()]
    query = session.query(Coche.combustible.distinct().label("combustible"))
    combustibles = [row.combustible for row in query.all()]
    query = session.query(Coche)
    models = []
    for m in marcas:
        models.append(query.filter(Coche.marca == m).all())
    
    print(models)
    return render_template("index.html", nCochesDonos=nCochesdonos, 
    nCochesBilbo=nCochesbilbo, 
    nCochesVito=nCochesvito, 
    arrCoches=coches, 
    arrMarcas=marcas, 
    ciudades=ciudades, 
    combustibles=combustibles,
    models=models
    )
