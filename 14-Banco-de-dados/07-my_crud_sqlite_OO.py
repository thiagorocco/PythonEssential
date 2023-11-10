'''
    Operações de CRUD com o banco de dados Sqlite orientado a objetos
'''
import sqlite3

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    @staticmethod
    def connect():
        conn = sqlite3.connect('database.db')
        return conn
    
    @staticmethod
    def create_table():
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                )
                    ''')
        conn.commit()
        conn.close()
    
    def create(self):
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users(name, email) VALUES (?, ?)',(self.name, self.email))
        conn.commit()
        conn.close()
    
    @staticmethod
    def read():
        pass
     