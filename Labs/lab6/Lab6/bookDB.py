import book
import pickle


class bookDB:
        def __init__(self, name):
                self.name = name
                try:
                        f = open('bd_dump'+name, 'rb')
                        self.bib = pickle.load(f)
                        f.close()
                        #for b in self.bib:
                        #        try:
                        #                b.likes+=0
                        #        except:
                        #                b.likes=0
                        for b in self.bib:
                                if hasattr(b,"likes"):
                                        b.likes=0

                except IOError:
                        self.bib = {}
        
        def authors(self) :
                authors = set()

                for x in self.bib :
                	authors.add(self.bib[x].author)
                return list(authors)


        def addBook(self, author, title, year):
                b_id = len(self.bib)
                self.bib[b_id] = book.book(author, title, year, b_id)
                f = open('bd_dump'+self.name, 'wb')
                pickle.dump(self.bib, f)
                f.close()
        def showBook(self, b_id):
                return self.bib[b_id]

        def listAllBooks(self):
                return list(self.bib.values())

        def listBooksAuthor(self, authorName):
                ret_value = []
                for b in self.bib.values():
                        if b.author == authorName:
                                ret_value.append(b)
                return ret_value
        def listBooksYear(self, year):
                ret_value = []
                for b in self.bib.values():
                        if b.year == year:
                                ret_value.append( b)
                return ret_value

        # retorna um vetor de livros de um certo author num dado ano
        def booksbyauthorinyear(self, author, year):
                ret_value = []
                for b in self.bib.values():
                        if b.year == year:
                                if b.author== author:
                                        ret_value.append(b)
                return ret_value

                

        def likeBook(self, id):
                for b in self.bib.values():
                        if b.id == id:
                                return b.likes
                        
                return 2


