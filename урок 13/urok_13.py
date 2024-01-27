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
sql.execute("")
# даём команды нашей базе данных

