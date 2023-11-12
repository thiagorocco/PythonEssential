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
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        conn.close()
        users = []
        for row in rows:
            user = User(row[1],row[2])
            user.id = row[0]
            users.append(user)
        return users

    @staticmethod
    def get_by_id(user_id):
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id))
        row = cursor.fetchone()
        conn.close()
        if row:
            user = User(row[1], row[2])
            user.id = row[0]
            return user
        return None
    
    def update(self):
        conn = User.connect()
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?',(self.name, self.email, self.id))
        conn.commit()
        conn.close()