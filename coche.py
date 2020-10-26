from base import Base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
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
