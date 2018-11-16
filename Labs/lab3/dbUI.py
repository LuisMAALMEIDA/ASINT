import bookDB
from book import book
class dbUI:
    bookarray = []

    def __init__(self, book_db):
        self.bookarray = book_db

    def readsFromKeyboard(self):

        notexit= True
        while notexit:

            command = input(">> ")

            if (command == "NEW"):
                print("Insert an author:")
                author = input(">> ")
                print("Insert an title:")
                title = input(">> ")
                print("Insert the published year:")
                pub_year = input(">> ")
                print("Insert a id:")
                id = input(">> ")
                b1=book(author, title, pub_year, id)
                self.bookarray.insert_book(b1)
            elif (command == "SHOW"):
                print("Insert the id:")
                id = input(">> ")
                self.bookarray.show_book(id)
            
            elif (command == "AUTHORS"):
                self.bookarray.list_authors()

            elif (command == "SEARCH_AUTHR"):
                print("Insert the name of a author")
                author= input(">> ")
                self.bookarray.print_book_of_author(author)

            elif (command == "SEARCH_YEAR"):
                print("Insert the year")
                year= input(">> ")
                self.bookarray.print_book_of_year(year)

            elif( command == "QUIT"):
                notexit = False