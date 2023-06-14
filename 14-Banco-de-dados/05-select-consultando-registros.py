'''
    Consultando registros no banco de dados

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

def consulta(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        resultado=c.fetchall()
        return resultado
    except Error as ex:
        print(ex)

vcon = dbConnection()
vsql = f"SELECT * FROM tb_contatos"


res = consulta(vcon, vsql)
for r in res:
    print(f'{r[0]}\t{r[1]}\t{r[2]}')