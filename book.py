import csv
class Book():
    def __init__(self, book_id, book_name, title, author, quantity, pub_year, edition):
        self.book_id = book_id
        self.book_name = book_name
        self.title = title
        self.author = author
        self.quantity = quantity
        self.pub_year = pub_year
        self.edition = edition

    def add_book(self):
        book_data = "{},{},{},{},{},{},{}\n".format(self.book_id, self.book_name, self.title, self.author, self.quantity, self.edition, self.pub_year)
        found = self.search_book_by_title(self.title)
        if not found:
            with open("book_data.csv", "a+") as file:
                file.write(book_data)
            print('--------------------------')
            print("Book added successfully!")
            print('---------------------------')
        else:
            print('--------------------------')
            print("Book already exists!!!")
            print('--------------------------')
    def search_book_by_title(self, title):
        found = False
        with open("book_data.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",")
                if book_info[2] == title:
                    found = True
                    return found
            if not found:
                return found
   
