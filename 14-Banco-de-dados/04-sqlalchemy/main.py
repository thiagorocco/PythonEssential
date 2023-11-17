from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criar uma instância do mecanismo SQLAlchemy e conectar-se a um banco de dados SQLite em memória
engine = create_engine('sqlite:///banco.db', echo=True)

# Criar uma classe de modelo para a tabela 'usuarios'
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)

# Criar a tabela no banco de dados
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Operações CRUD

# Create (Criar um novo usuário)
novo_usuario = Usuario(nome='John Doe', idade=25)
session.add(novo_usuario)
session.commit()

# Read (Consultar todos os usuários)
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}')

# Update (Atualizar um usuário)
usuario_para_atualizar = session.query(Usuario).filter_by(nome='John Doe').first()
if usuario_para_atualizar:
    usuario_para_atualizar.idade = 26
    session.commit()

# Read (Consultar novamente após a atualização)
usuarios_atualizados = session.query(Usuario).all()
for usuario in usuarios_atualizados:
    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}')

# Delete (Excluir um usuário)
usuario_para_excluir = session.query(Usuario).filter_by(nome='John Doe').first()
if usuario_para_excluir:
    session.delete(usuario_para_excluir)
    session.commit()

# Read (Consultar novamente após a exclusão)
usuarios_apos_exclusao = session.query(Usuario).all()
if not usuarios_apos_exclusao:
    print('Nenhum usuário encontrado após a exclusão.')

# Fechar a sessão
session.close()
