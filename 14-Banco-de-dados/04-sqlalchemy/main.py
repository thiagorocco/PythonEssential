from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Criar uma instância do mecanismo SQLAlchemy e conectar-se a um banco de dados SQLite em memória
engine = create_engine('sqlite:///banco.db', echo=False)

# Criar uma classe de modelo para a tabela 'usuarios'
Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    idade = Column(Integer)

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

class Crud:

    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=engine)

    def create(self, nome, idade):
        session = self.Session()
        novo_usuario = UserModel(nome=nome, idade=idade)
        session.add(novo_usuario)
        session.commit()
        session.close()

    def read(self):
        session = self.Session()
        usuarios = session.query(UserModel).all()
        for usuario in usuarios:
            print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}')
        session.close()    

    def update(self, id, nome, idade):
        session = self.Session()
        usuario_para_atualizar = session.query(UserModel).filter_by(id=id).first()
        if usuario_para_atualizar:
            usuario_para_atualizar.nome = nome
            usuario_para_atualizar.idade = idade
            session.commit()
        session.close()


    def delete(self, id):
        session = self.Session()
        usuario_para_excluir = session.query(UserModel).filter_by(id=id).first()
        if usuario_para_excluir:
            session.delete(usuario_para_excluir)
            session.commit()
        session.close()


os.system('clear') or None
usuario = Crud(engine)
usuario.create('Peninha',70)
usuario.read()



