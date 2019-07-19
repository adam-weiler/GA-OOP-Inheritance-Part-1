class Person():
    def __init__ (self, name):
        self.name = name

    def greeting(self):
        return f'{self.name}: Hi, my name is {self.name}!'

class Student(Person):  
    def learn(self):
        return f'{self.name}: I get it!'

class Instructor(Person):
    def teach(self):
        return f'{self.name}: An object is an instance of a class.'

nadia = Instructor('Nadia')
chris = Student('Chris')

print(nadia.greeting())
print(chris.greeting())
print(nadia.teach())
print(chris.learn())