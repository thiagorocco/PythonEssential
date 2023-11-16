'''
    Excluindo registros no banco de dados

    CUIDADO ao usar DELETE! 
    Se executar esse comando "DELETE FROM nome_tabela" vai excluir todos os registros!
    Sempre após o nome da tabela insera o WHERE
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

def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro excluído')


vcon = dbConnection()
vsql = f"DELETE FROM tb_contatos WHERE N_IDCONTATO=2"
deletar(vcon, vsql)
