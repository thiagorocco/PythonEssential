'''
    Inserindo registros no banco de dados
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

def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

nome = input('Digite o nome: ')
telefone = input('Digite o telefone: ')
email = input('Digite o email: ')

vcon = dbConnection()

vsql = f"""INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
          VALUES('{nome}','{telefone}','{email}')"""

inserir(vcon,vsql)
