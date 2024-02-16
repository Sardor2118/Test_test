import sqlite3
from datetime import datetime

connection = sqlite3.connect("baza_dannix.db")
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT, work TEXT,'
            'phone_number TEXT, language TEXT, reg_date DATETIME);')

def add_user(user_id, user_name, user_phone_number, user_work):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    (sql.execute('INSERT INTO users (user_id, name, phone_number, reg_date, work) VALUES (?, ?, ?, ?, ?);')
     (user_id, user_name, user_phone_number, user_work, datetime.now()))
def get_users():
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    users = sql.execute('SELECT * FROM users;').fetchall()
    return users
def check_users(user_id):
    connection = sqlite3.connect("baza_dannix.db")
    sql = connection.cursor()
    checker = sql.execute('SELECT user_id FROM users WHERE user_id = ?;',(user_id, )).fetchone()
    if checker:
        return True
    else:
        return False
