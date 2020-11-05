from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:root@localhost:5432/bustomoviles')
#engine = create_engine('postgres://bpyzodwvtsscct:309b4d8d7d7fc8d61715e4e9bec4f61b94ba84406ec4b327c52b7924a5137607@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/d255l5nmsmvmo9')

Session = sessionmaker(bind=engine)

Base = declarative_base()
