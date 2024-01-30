import sqlite3
connection1 = sqlite3.connect('users.db')
sql = connection1.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')
sql.execute('INSERT INTO users (user_id, username) VALUES (1992, "Sardor");')



id_users = sql.execute('SELECT user_id FROM users;').fetchall()
print(id_users)
where = sql.execute('SELECT * FROM users WHERE username="Sardor";').fetchall()
print(where)
# delete = sql.execute('DELETE FROM users;')
# print(delete)


eba = sql.execute('UPDATE users SET username="SWW" WHERE user_id=1992;')
print(eba)

connection1.commit()