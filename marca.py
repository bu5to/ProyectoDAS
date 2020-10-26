from base import Base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Marca(Base):
    __tablename__ = 'marca'
    id = Column(Integer, primary_key=True)
    marca = Column(String(20), unique=True)
    pais = Column(String(20))
    coches = relationship("Coche")

    def __init__(self, marca, pais):
        self.marca = marca
        self.pais = pais