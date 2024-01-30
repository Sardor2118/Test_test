# SQL данные
# integer = целые числа
# real = десятичные дроби (float)
# text = текстовые значения (str)
# import sqlite3
# sqlite3.connect('card.db')

import sqlite3
# импортируем библиотеку sql
connection = sqlite3.connect('my_users.db')
# подключаемся к базе данных
sql = connection.cursor()
# создаем использинеля для работы с sql
sql.execute('CREATE TABLE cars (name TEXT, model TEXT, year INTEGER);')
# даём команды нашей базе данных
connection.commit()
# сохранение данных после изменений
connection.close()
# закрываем соеденение с базой данных

# SELECT - выбирает колонку чтобы получить данных из таблицы
# FROM - выбирает таблицу из которой выбрать данные
# WHERE - фильтрация искать в колоннах
# UPDATE - обновление колон в таблице
# SET - новое значение чтобы обновить

# .execute('CREATE TABLE cars (name TEXT, model TEXT, year INTEGER);')
# sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')
# sql.execute('UPDATE cars SET year=2011 WHERE model='tesla';)

