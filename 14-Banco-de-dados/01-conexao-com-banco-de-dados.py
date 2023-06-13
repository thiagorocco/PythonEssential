from multiprocessing import connection
import sqlite3
from sqlite3 import Error

#Criar conexão
def dbConnection():
    path = '14-Banco-de-dados\\agenda.db'
    connection = None    
    try:
        connection = sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return connection
    
vcon = dbConnection()

vsql = """CREATE TABLE tb_contatos(
    N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30),
    T_TELEFONECONTATO VARCHAR(14),
    T_EMAILCONTATO VARCHAR(30)
);"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)
vcon.close()
