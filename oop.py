## OOP Programming
# class User():
#     pass

# instance = User()

# print(type(instance))

# class User():
#     def __init__(self, username, email, password, name, surname):
#         self.username = username
#         self.email = email
#         self.password = password,
#         self.name = name,
#         self.surname = surname
#         pass

# instance = User('joshuabritz', 'joshuabritz@gmail.com', 'password1234', 'Joshua', 'Britz')

# print(instance)

# class Cirlce():
#     PI = 3.14

#     def __init__(self, radius=1):
#         self.radius = radius

#     def get_circumference(self):
#         return round(self.radius * self.PI * 2, 2)

# my_circle = Cirlce(20)

# print(my_circle.get_circumference())

# class Animal():
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError('Subclass has not implemented this method')

# class Dog(Animal):
#     def speak(self):
#         print(f'{self.name} says woof')

# class Cat(Animal):
#     def speak(self):
#         print(f'{self.name} says meow')

# my_cat = Cat('Felix')
# my_dog = Dog('Nico')

# my_cat.speak()
# my_dog.speak()


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return str({
            'title': self.title,
            'author': self.author,
            'full': f'{self.title} by {self.author}'
        })

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f'{self.title} by {self.author} was deleted')


book = Book('Lord of the Rings', 'JRR Tolkien', 800)

print(book)
print(len(book))
del book