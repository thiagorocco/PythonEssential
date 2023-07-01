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

    #Aqui obtemos o caminho absoluto do diretório do nosso código e conectamos ou criamos
    #o nosso banco de dados no mesmo local. Independente do sistema operacional
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
        sql = f'CREATE TABLE {tabela}('
        for campo in campos.keys():
            if i < tam:
                sql += f'{campo} {campos[campo]},'
            else:
                sql += f'{campo} {campos[campo]}'
            i += 1    

        sql += ');'
        cursor.execute(sql)
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
        sql = f"INSERT INTO {tabela} ({campos}) VALUES ({valores})"
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print('Produto cadastrado com sucesso!')
    except Error as ex:
        print(f'Erro de execução = {ex}')
def read(conn,tabela):
    try:
        sql = f'SELECT * FROM {tabela}'
        cursor = conn.cursor()
        cursor.execute(sql)

        resultado = cursor.fetchall()
        for r in resultado:
            print(r)
        conn.close() 
    except Error as ex:
        print(f'Erro de conexão: {ex}')

def edit(conn, tabela, campos, id):
    try:
        sql = f"UPDATE {tabela} SET {campos} WHERE id={id}"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print('Produto alterado com sucesso')
    except Error as ex:
        print('Erro: ',ex)

def delete(conn, tabela, id):
    try:
       sql = f"DELETE FROM {tabela} WHERE id={id}"
       cursor = conn.cursor()
       cursor.execute(sql)
       conn.commit()
       conn.close()
       print('Produto excluído com sucesso!')     
    except Error as ex:
        print('Erro: ',ex)

'''
tabela = 'produtos'
campos = {'id':'INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL',
          'prod':'VARCHAR(80)',
          'preco':'DOUBLE(5,2)'}
prod = 'Caderno'
preco = 24.99
'''

#conectar()
#createTable(conectar(),tabela,campos)
#create(conectar(),tabela,["prod","preco"],[f"'{prod}'",f"'{preco}'"])
#read(conectar(),tabela)
#edit(conectar(),tabela,"prod='Casaco',preco='224.99'",2)
#delete(conectar(),tabela,3)

while True:
    os.system('clear')or None
    print('*** CRUD COM SQLITE ***')
    print()
    print('1 - Inserir novo produto')
    print('2 - Listar produtos cadastrados')
    print('3 - Alterar um produto')
    print('4 - Excluir um produto')
    print('5 - Sair')

    op = input('Digite a opção desejada: ')

    #match ... case, só vai funcionar no python a partir da versão 3.10
    match op:
        case '1':
            while True:
                os.system('clear')or None
                print('*** Cadastro de produto ***')
                try:
                    prod = input('Nome do novo produto: ')
                    preco = float(input('Preço do novo produto: '))
                    create(conectar(),'produtos',["prod","preco"],[f"'{prod}','{preco}'"])
                    input('Pressione qualquer tecla para continuar')
                    break
                except:
                    print("Por favor insira apenas números no preço e separe as casas decimais com ponto(.)")
                    input('Pressione qualquer tecla para continuar')
        case '2':
            os.system('clear')or None
            print('Listando os produtos cadastrados')
            print('')
            print("ID   |   DESCRIÇÃO   |   PREÇO")
            read(conectar(),'produtos')
            input('Pressione qualquer tecla para continuar')
        case '3':
            os.system('clear')or None
            print('Alteração de produto')
            read(conectar(),'produtos')
            input('Informe o código(ID) do produto que deseja alterar: ')
            input()
            #edit()
        case '4':
            os.system('clear')or None
            print('Exclusão de produto')
            input()
            #delete()
        case '5':
            break
        case _:
            os.system('clear')or None
            print('Opção inválida. Digite uma das opção acima de 1 a 5')
            input()




