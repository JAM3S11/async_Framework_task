class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
        print('\n')
        print(f'Hello, my name is {self.name}.')
        print(f'I am {self.age} years old and I am a {self.gender}.')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
gender = input('Enter your gender: ')

# object creation
person = Person(name, age, gender)
person.introduction()
