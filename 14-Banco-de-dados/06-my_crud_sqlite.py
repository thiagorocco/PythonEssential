'''
    cursor: é um interador que permite navegar e manipular os registros do bd.
    execute: lê e executa comandos SQL puro diretamente no bd.
    commit - grava as informações no banco de dados

    Após qualquer interação com o banco de dados feche a conexão com close()
'''
import sqlite3
from sqlite3 import Error

#Conexão e/ou criação do banco de dados
def conectar():
    caminho = 'banco-de-dados\\baseSqlite.db'
    try:
        conn = sqlite3.connect(caminho)
        return conn
    except:
        print('Falha na conexão com o banco de dados')

#Criação de Tabelas
def createTable(conn,tabela,campos):
    try:
        cursor = conn.cursor()
        tam = len(campos)
        i = 1
        instruction = f'CREATE TABLE {tabela}('
        for campo in campos.keys():
            if i < tam:
                instruction += f'{campo} {campos[campo]},'
            else:
                instruction += f'{campo} {campos[campo]}'
            i += 1    

        instruction += ');'
        cursor.execute(instruction)
        conn.close()
        print(f'Tabela {tabela} cadastrada com sucesso!')
    except Error as ex:
        print(f'Erro de execução = {ex}')

#### CRUD - Operações de criação, leitura, edição(alteração) e exclusão dos registros ####

def create(conn,tabela,dados):
    try:
        c = conn.cursor()
        #usar um método explode para pegar chaves e valores de dados
        #depois ver quantos campos de chave e valor tem para inserir na instrução abaixo
        instruction = f'INSERTO INTO {tabela}() VALUES ()'
        print('Registro inserido com sucesso!')
    except Error as ex:
        print(f'Erro de execução = {ex}')
def read(conn):
    print()

def edit(conn, id):
    print()

def delete(conn, id):
    print()

tabela = 'produtos'
campos = {'id':'integer auto increment',
          'prod':'varchar(80)',
          'preco':'double(5,2)'}

#createTable(conectar(),tabela,campos)
