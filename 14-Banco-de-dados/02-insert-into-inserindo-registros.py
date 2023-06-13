'''
    Inserindo registros no banco de dados
'''
import sqlite3
from sqlite3 import Error

def dbConnection():
    path = '14-Banco-de-dados\\agenda.db'
    connection = None    
    try:
        connection = sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return connection

vcon = dbConnection()

nome = input('Digite o nome: ')
telefone = input('Digite o telefone: ')
email = input('Digite o email: ')

vsql = f"""INSERT INTO tb_contatos
            (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO)
          VALUES('{nome}','{telefone}','{email}')"""
def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

inserir(vcon,vsql)