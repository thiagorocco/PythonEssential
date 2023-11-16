'''
    Atualizando/Editando registros no banco de dados

'''
import sqlite3
from sqlite3 import Error

def dbConnection():
    path = 'agenda.db'
    connection = None    
    try:
        connection = sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return connection

def atualizar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro atualizado')


vcon = dbConnection()
vsql = f"UPDATE tb_contatos SET T_NOMECONTATO='Thiago de Rocco',T_TELEFONECONTATO='4188888888',T_EMAILCONTATO='deroccotr@gmail.com' WHERE N_IDCONTATO=1"
atualizar(vcon, vsql)
