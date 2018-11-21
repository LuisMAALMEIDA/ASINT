from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
import bookDB

class Storage:
    def __init__ (self):
        self.data = {}
    def getSize(self):
        return len(self.data)
    def store(self, val):
        try:
            self.data[val] +=1
        except:
            self.data[val] = 1
    def getKeys(self):
        return self.data.keys()
    def getValue(self, key):
        try:
            return self.data[key]
        except:
            return None

app = Flask(__name__)
st = Storage()
db = bookDB.bookDB("mylib")

@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books=count)

@app.route('/addBooksForm')
def add_Book_Form():
    return render_template("addBookTemplate.html")

@app.route('/addBook', methods=['POST', 'GET'])
def add_Book():
    if request.method == "GET":
        author= request.args.get('Author')
        title= request.args.get('Title')
        year= request.args.get('Year')
        db.addBook(author, title, year)
        print (author)
        print(title)
        print(year)
        return render_template("addBookTemplate.html")
    else:
        author= request.form.get('Author')
        title= request.form.get('Title')
        year= request.form.get('Year')
        db.addBook(author, title, year)
        return render_template("addBookTemplate.html")
        
    
    
@app.route('/listAllBooks')
def listAllBooka():
    books=db.listAllBooks()
    return render_template("listAllBooks.html", bookss= books)

@app.route('/showBookForm')
def show_Book_Form():
    return redirect("static/showBookTemplate.xhtml" )

@app.route('/showBook', methods=['GET'])
def show_Book():
    if request.method == "GET":
       id =request.args.get('id')

    book = db.showBook(int(id))

    return render_template("showBook.html" ,book= book)


@app.route('/listBooksAuthorForm')
def listBooksAuthorForm():
    return render_template("listBooksAuthorForm.html" )

@app.route('/listBooks', methods=['GET'])
def listBooksAuthor():
    if request.method == "GET":
        author =request.args.get('author')
        books = db.listBooksAuthor(author)
    return render_template("listBooks.html" ,books= books)


@app.route('/listBooksYearForm')
def listBooksYearForm():
    return render_template("listBooksYearForm.html" )

@app.route('/listBooksYear', methods=['GET'])
def listBooksYear():
    if request.method == "GET":
        year =request.args.get('year')
        books = db.listBooksYear(int(year))
    return render_template("listBooks.html" ,books= books)

########### client endpoints    
@app.route('/API/Books')
def API_showbooks():
    list_b = db.listAllBooks()
    nl = list(map(lambda x: x.toDict(), list_b) )
	
    return jsonify(str(nl))

@app.route('/API/addBook', methods=['POST'])
def API_add_Book():
    
    content = request.json
    author = content['Author']
    title = content['Title']
    year = content['Year']
    db.addBook(author, title, year)
    return str(200)


@app.route('/API/listBooksAuthor', methods=['POST'])
def API_listBooksAuthor():
    
    content = request.json
    author = content['Author']
    books = db.listBooksAuthor(author)
    nl = list(map(lambda x: x.toDict(), books) )
    return jsonify(str(nl))


@app.route('/API/showbook', methods=['POST'])
def API_showbook():
    
    content = request.json
    book_id = content['BookID']
    book = db.showBook(book_id)
    nl = book.toDict() 

    return jsonify(str(nl))


#Lista todos os livros de um certo ano
@app.route('/API/listBooksYear', methods=['POST'])
def API_listBooksYear():
    
    content = request.json
    year = content['Year']
    books= db.listBooksYear(year)
    nl = list(map(lambda x: x.toDict(), books) )

    return jsonify(str(nl))

#Lista todos os livros de um certo ano
@app.route('/API/booksbyauthorinyear', methods=['POST'])
def API_booksbyauthorinyear():
    
    content = request.json
    author = content['Author']
    year = content['Year']
    books= db.booksbyauthorinyear(author, year)
    print(books)
    nl = list(map(lambda x: x.toDict(), books) )

    return jsonify(str(nl))       

######### cenas dos likes

@app.route('/API/Books/<id>/likes', methods=['POST'])
def f_like(id):

    nlikes=db.likeBook(id)
    book= db.showBook(id)
    return jsonify({"likes": nl})


if __name__ == '__main__':
    app.run()
