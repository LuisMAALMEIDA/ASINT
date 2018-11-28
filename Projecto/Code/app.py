from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect


app = Flask(__name__)
buildings = Building()
storage = Storage()
logs = logs()

def AuthenticateAdmin(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False

# Admin endpoints

@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books=count)

@app.route('/addBooksForm')
def add_Book_Form():
    return render_template("addBookTemplate.html")



        

if __name__ == '__main__':
    app.run()
