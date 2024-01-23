class User:
    def __init__(self, name, email, age, number):
        self.name = name
        self.email = email
        self.age = age
        self.number = number

    def change_name(self, new_name):
        self.color = new_name

    def change_email(self, new_email):
        self.email = new_email

    def change_age(self, new_age):
        self.age = new_age

    def change_number(self, new_number):
        self.number = new_number
