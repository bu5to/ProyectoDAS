from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, SignupForm
from sqlalchemy import create_engine, and_, Column, String, Integer, ForeignKey, select, func
from sqlalchemy.orm import relationship
from base import Base, Session
from models import Coche, Marca, get_users, User, get_user, Comentario
from werkzeug.urls import url_parse
import numpy as np
import functools
from inserts import create_tables
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['DATABASE_URL'] = "postgres://bpyzodwvtsscct:309b4d8d7d7fc8d61715e4e9bec4f61b94ba84406ec4b327c52b7924a5137607@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/d255l5nmsmvmo9"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/bustomoviles'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bpyzodwvtsscct:309b4d8d7d7fc8d61715e4e9bec4f61b94ba84406ec4b327c52b7924a5137607@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/d255l5nmsmvmo9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bu5t0m0viles@gmail.com'
app.config['MAIL_PASSWORD'] = 'joseaspasromano'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.cli.add_command(create_tables)
login_manager = LoginManager(app)
login_manager.login_view = "login"
mail = Mail(app)
session = Session()
session.expire_on_commit = False 

@app.route('/', methods=['GET'])
def index():
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
    query = session.query(Comentario)
    comentarios = query.all()
    query = session.query(Marca)
    marcas = query.all()
    query = session.query(Coche.ciudad.distinct().label("ciudad"))
    ciudades = [row.ciudad for row in query.all()]
    query = session.query(Coche.combustible.distinct().label("combustible"))
    combustibles = [row.combustible for row in query.all()]
    query = session.query(Coche)
    models = []
    for m in marcas:
        models.append(query.filter(Coche.marca == m).distinct(Coche.modelo)) 

    return render_template("index.html", nCochesDonos=nCochesdonos, 
            nCochesBilbo=nCochesbilbo, 
            nCochesVito=nCochesvito, 
            arrCoches=coches, 
            arrMarcas=marcas, 
            ciudades=ciudades, 
            combustibles=combustibles,
            models=models,
            comentarios=comentarios
            )
    
@app.route("/enviar", methods=['GET', 'POST'])
def enviar():
    value = request.form['copia'] 
    strmensaje = request.form['mensaje']
    dest = request.form['email']
    nombre = request.form['nombre']
    if (strmensaje!='' and nombre!=''):
        sesEmail = Session()
        co = Comentario(nombre, strmensaje)
        sesEmail.add(co)
        sesEmail.commit()
        sesEmail.close()
    if value == "Sí":
        mensaje = "¡Hola, " + nombre + "! Esta es una copia automática de tu sugerencia generada por Bustomóviles. ¡Te responderemos en breve!\n" + strmensaje + "\n Un cordial saludo,\n Jorge El Busto - Fundador de Bustomóviles"
        msg = Message('Bustomóviles - Copia de tu mensaje', sender = 'bu5t0m0viles@gmail.com', recipients = [dest])
        msg.body = mensaje
        mail.send(msg)
        return redirect("contact")
    else:
        return redirect("contact")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        print(user)
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
        users = get_users()
        user = User(len(users) + 2, name, email, password)
        session.add(user)
        session.commit()
        session.close()
        # users.append(user)
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

@app.route('/coche/<int:coche_id>')
def coche(coche_id):  
    query = session.query(Coche)
    query = query.filter(Coche.id==coche_id).first()
    if request.method == 'POST':
        session.delete(query)
        return redirect(url_for('index'))
    else:
        return render_template("coche.html", coche = query)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    search = request.form['search']
    if request.form['marca'] != 'Marca':
        marca=request.form['marca']
    else:
        marca=''
    if request.form['modelo'] != 'Modelo':
        modelo=request.form['modelo']
    else:
        modelo=''
    if request.form['ciudad'] != 'Todas las ciudades':
        ciudad=request.form['ciudad']
    else:
        ciudad=''
    if request.form['combustible'] != 'Combustible':
        combustible=request.form['combustible']
    else:
        combustible=''
    precio = request.form['precio']
    if request.form['km'] != 'Kilómetros':
        km=request.form['km']
    else:
        km = ''
    resultados =[]
    session = Session()
    qDesc = session.query(Coche)
    qDesc = qDesc.filter(Coche.descripcion.like("%"+search+"%")).all()

    qMarca = session.query(Coche).join(Marca)
    if marca != '':
        qMarca = qMarca.filter(Marca.marca == marca).all()
    else:
        qMarca = qMarca.all()
    qModelo = session.query(Coche)
    if modelo != '':
        qModelo = qModelo.filter(Coche.modelo == modelo).all()
    else:
        qModelo = qModelo.all()
    qCiudad = session.query(Coche)
    if ciudad != '':
        qCiudad = qCiudad.filter(Coche.ciudad == ciudad).all()
    else: 
        qCiudad = qCiudad.all()
    qCombustible = session.query(Coche)
    if combustible != '':
        qCombustible = qCombustible.filter(Coche.combustible == combustible).all()
    else:
        qCombustible = qCombustible.all()
    qPrecio = session.query(Coche)
    qPrecio = qPrecio.filter(Coche.precio < precio).all()
    qKm = session.query(Coche)
    if km == '10k':
        qKm = qKm.filter(Coche.kilometros < 10000).all()
    elif km == '1050k':
        qKm = qKm.filter(and_(Coche.kilometros > 10000, Coche.kilometros<50000)).all()
    elif km == '50100k':
        qKm = qKm.filter(and_(Coche.kilometros > 50000, Coche.kilometros<100000)).all()
    elif km == '100200k':
        qKm = qKm.filter(and_(Coche.kilometros > 100000, Coche.kilometros<200000)).all()
    elif km == '200300k':
        qKm = qKm.filter(and_(Coche.kilometros > 200000, Coche.kilometros<300000)).all()
    elif km == '300k':
        qKm = qKm.filter(Coche.kilometros > 300000).all()

    
    if request.form['potMinima'] == '':
        potMinima = 0
    else:
        potMinima = request.form['potMinima']
    if request.form['potMaxima'] == '':
        potMaxima = 1600
    else:
        potMaxima = request.form['potMaxima']
    qPot = session.query(Coche)
    qPot = qPot.filter(and_(Coche.potencia >= potMinima, Coche.potencia <= potMaxima)).all()

    if request.form['anodesde'] == '':
        anoDesde = 1900
    else:
        anoDesde = request.form['anodesde']
    if request.form['anohasta'] == '':
        anoHasta = 2021
    else:
        anoHasta = request.form['anohasta']
    qAnyo = session.query(Coche)
    qAnyo = qAnyo.filter(and_(Coche.anyo >= anoDesde, Coche.anyo <= anoHasta)).all()

    resultados = list(set(qMarca) & set(qDesc) & set(qModelo) & set(qCiudad) & set(qCombustible) & set(qPrecio) & set(qKm) & set(qPot) & set(qAnyo))
    return render_template("coches.html", busqueda = resultados)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/vender', methods=['GET', 'POST'])
def vender():
    if current_user.is_authenticated:
        sesQuery = Session()
        query = sesQuery.query(Marca)
        paises = [row.pais for row in query.distinct(Marca.pais)]
        marcas = [row.marca for row in query.all()]
        print(marcas)
        print(paises)
        sesQuery.close()
        if request.method == 'POST':
            strMarca = request.form['marca']
            if strMarca == '':
                print("No lo coge")
                strMarca = request.form['marcaselect']
            strPais = request.form['pais']
            if strPais == '':
                strPais = request.form['paisselect']
            session = Session()
            qMarca = session.query(Marca)
            qMarca = qMarca.filter(Marca.marca == strMarca).all()
            if len(qMarca) == 0:
                newMarca = Marca(strMarca, strPais)
                session.add(newMarca)
            else:
                newMarca = qMarca[0]
            modelo = request.form['modelo']
            anyo = request.form['anyo']
            combustible = request.form['combustible']
            potencia = request.form['potencia']
            kilometros = request.form['kilometros']
            precio = int(round(int(request.form['precio']) * 1.1))
            ciudad = request.form['ciudad']
            img = request.form['img']
            descripcion = request.form['descripcion']
            coche = Coche(newMarca, modelo, anyo, kilometros, combustible, potencia, descripcion, precio, ciudad, img)
            session.add(coche)
            session.commit()
            session.close()
            
            return render_template("vender.html", marcas=marcas, paises=paises)
        else:
            return render_template("vender.html", marcas=marcas, paises=paises)
    else:
        return redirect("signup")


@login_manager.user_loader
def load_user(user_id):
    users = get_users()
    for user in users:
        if user.id == int(user_id):
            return user
    return None

if __name__ == '__main__':
    app.run(debug == True)
    