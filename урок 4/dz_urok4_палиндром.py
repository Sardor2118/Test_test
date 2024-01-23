# Сделать программу, которая выводит только слова палиндромы (слова которые читаются в обе стороны)
# - пользователь должен вводить слово
# - получает ответ палиндром или нет

def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
#while True: можно добавить как цикл, чтобы проверить несколько слов
word = input("Введите слово: ")
result = is_palindrome(word)
if result:
    print("Это слово палиндром")
else:
    print("Это слово не палиндром")