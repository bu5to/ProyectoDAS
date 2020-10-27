from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, SignupForm
import mysql.connector
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, select, func
from sqlalchemy.orm import relationship
from base import Base, Session
from models import Coche, Marca, users, User, get_user
from werkzeug.urls import url_parse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/bustomoviles'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.route('/')
def index():
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
    
    return render_template("index.html", nCochesDonos=nCochesdonos, 
    nCochesBilbo=nCochesbilbo, 
    nCochesVito=nCochesvito, 
    arrCoches=coches, 
    arrMarcas=marcas, 
    ciudades=ciudades, 
    combustibles=combustibles,
    models=models
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, password)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None