import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY,name TEXT,age INTEGER,grade TEXT);")

cursor.execute("INSERT INTO students (name, age, grade) VALUES ('Алина', 19, 'A'), ('Борис', 20, 'B'), ('Виктор', 21, 'C'), ('Дарья', 18, 'A'), ('Егор', 22, 'D');")

conn.commit()
def get_student_by_name(name):
    sql = "SELECT name, age, grade FROM students WHERE name = ?"
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        return "Студент с таким именем не найден"

def update_student_grade(name, new_grade):
    sql = "UPDATE students SET grade = ? WHERE name = ?"
    cursor.execute(sql, (new_grade, name))
    conn.commit()
    if cursor.rowcount > 0:
        return "Оценка студента успешно обновлена"
    else:
        return "Студент с таким именем не найден"

def delete_student(name):
    sql = "DELETE FROM students WHERE name = ?"
    cursor.execute(sql, (name,))
    conn.commit()
    if cursor.rowcount > 0:
        return "Студент успешно удален"
    else:
        return "Студент с таким именем не найден"