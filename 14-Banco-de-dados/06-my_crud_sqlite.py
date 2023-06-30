'''
    cursor: é um interador que permite navegar e manipular os registros do bd.
    execute: lê e executa comandos SQL puro diretamente no bd.
    commit - grava as informações no banco de dados

    Após qualquer interação com o banco de dados feche a conexão com close()
'''
import os
import sqlite3
from sqlite3 import Error

#Conexão e/ou criação do banco de dados
def conectar():
    dir_codigo = os.path.dirname(os.path.abspath(__file__))
    nome_bd = 'baseSqlite.db'
    caminho = os.path.join(dir_codigo,nome_bd)

    try:
        conn = sqlite3.connect(caminho)
        return conn
    except Error as ex:
        print('Falha na conexão com o banco de dados: ',ex)

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

def create(conn,tabela,fields,values):
    try:
        cursor = conn.cursor()
        campos = ','.join(fields)
        valores = ','.join(values)
        instruction = f"INSERT INTO {tabela} ({campos}) VALUES ({valores})"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
        print('Registro inserido com sucesso!')
    except Error as ex:
        print(f'Erro de execução = {ex}')
def read(conn,tabela):
    try:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {tabela}')

        resultado = cursor.fetchall()
        for r in resultado:
            print(r) 
    except Error as ex:
        print(f'Erro de conexão: {ex}')

def edit(conn, id):
    print()

def delete(conn, id):
    print()

tabela = 'produtos'
campos = {'id':'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL',
          'prod':'VARCHAR(80)',
          'preco':'DOUBLE(5,2)'}

prod = 'Caderno'
preco = 24.99

#conectar()
#createTable(conectar(),tabela,campos)
#create(conectar(),tabela,["prod","preco"],[f"'{prod}'",f"'{preco}'"])
read(conectar(),tabela)
#update(conectar(),tabela,campos,id)
#delete