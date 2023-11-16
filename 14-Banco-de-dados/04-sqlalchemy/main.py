from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criar uma instância da engine SQLite e declarar a base
engine = create_engine('sqlite:///exemplo.db',echo=True)
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)