from base import Base
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    usuario = Column(String(20), unique=True)
    email = Column(String(30), unique=True)
    passwd = Column(String(80))

    def __init__(self, usuario, email, passwd):
        self.usuario = usuario
        self.email = email
        self.passwd = passwd