class Person():
    def __init__ (self, name):
        self.name = name

    def greeting(self):
        return f'Hi, my name is {self.name}.'




class Student(Person):
    
    def learn():
        return 'I get it!'

class Instructor(Person):
    
    def teach():
        return 'An object is an instance of a class.'


nadia = Instructor('Nadia')
print(nadia.greeting())

