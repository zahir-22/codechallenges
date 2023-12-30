# creating a library for users

# books class
class Books:
    def __init__(self, title, content, pages):
        self.title = title
        self.content = content
        self.pages = pages

    def add_books(self, title):
        add_book = input('enter book name to add:')
        title.append(add_book)

    def delete_b(self, title):
        del title


class Library:
    def __init__(self, books, department, stuff):
        self.books = books
        self.department = department
        self.stuff = stuff


class Users:
    def __init__(self, user_id, name, gender):
        self.user_id = user_id
        self.name = name
        self.gender = gender










