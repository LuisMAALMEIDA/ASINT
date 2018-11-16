from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import bookDB

app = Flask(__name__)
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
    return render_template("showBookTemplate.html" )

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
    title = content['Title']
    year = content['Year']
    db.addBook(author, title, year)
    return str(200)
        

######### cenas dos likes

@app.route('/API/Books/<id>/likes', methods=['POST'])
def f_like(id):

    nl=db.likeBook(id)
    return jsonify({"likes": nl})


if __name__ == '__main__':
    app.run()
