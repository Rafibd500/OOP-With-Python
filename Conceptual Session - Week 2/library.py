class User:
    def __init__(self,id, name, password):
        self.id = id
        self.name = name
        self.password = password
class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []
    def addUser(self, name, quantity):
        id = len(self.users)+1001
        user = User(id, name, quantity)
        self.users.append(user)
        print(f"User {name} added successfully.")
        return user
    def addBook(self, name, quantity):
        id = len(self.books)+ 2001
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f'{name} book added successfully.')
        return book

