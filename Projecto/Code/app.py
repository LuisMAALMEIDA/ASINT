from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from Building import Building

app = Flask(__name__)
buildings =  Building()
storage = Storage()
logs = Logs()

def AuthenticateAdmin(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False

############### Admin endpoints ###############
###############################################

# Creates a building specified by the admin
@app.route('/API/Admin/CreateBuilding')
def CreateBuilding():
    # TODO
    return render_template("mainPage.html", count_books=count)

# List all buildings on the server
@app.route('/API/Admin/ListBuildings')
def ListBuildings():
    # TODO
    return render_template("mainPage.html", count_books=count)

# List all users on the server
@app.route('/API/Admin/ListUsers')
def ListLoggedUsers():
    # TODO
    return render_template("mainPage.html", count_books=count)

# List all users in a building on the server
@app.route('/API/Admin/ListUsers/<BuidingID>')
def ListLoggedUsers(BuidingID):
    # TODO
    return render_template("mainPage.html", count_books=count)

# List all the logs from a specified user
@app.route('/API/Admin/Logs/<User>')
def ListLoggedUsers(User):
    # TODO
    return render_template("mainPage.html", count_books=count)

# List all the logs from a specified buiding
@app.route('/API/Admin/Logs/<BuidingID>')
def ListLoggedUsers(BuidingID):
    # TODO
    return render_template("mainPage.html", count_books=count)



############### Webrowser endpoints ###############
###################################################
@app.route('/')
def hello_world():
    count = len(db.listAllBooks())
    return render_template("mainPage.html", count_books=count)

# Authenticate the user
@app.route('/API/Users/FenixAuthentication')
def FenixAuthentication():
    # TODO
    return render_template("mainPage.html", count_books=count)

# Logout the user
@app.route('/API/Users/Logout')
def Logout():
    # TODO
    return render_template("mainPage.html", count_books=count)    

# Send messages to users nearby the User (UserId) who request this servive 
@app.route('/API/Users/SendMessage/<UserId>')
def SendMessageToNearbyUsers(UserId):
    # TODO
    return render_template("mainPage.html", count_books=count)

# Define the range that will include the nearby users
@app.route('/API/Users/DefineRange/<UserId>')
def DefineRange(UserId):
    # TODO
    return render_template("mainPage.html", count_books=count)       

# List the nearby useres: on the range of the messages and on
# the same building
@app.route('/API/Users/NearbyUsers/<UserId>')
def ListNearbyUsers(UserId):
    # TODO
    return render_template("mainPage.html", count_books=count) 

#Send the messages to the user sent by other users and bots
@app.route('/API/Users/ReceiveMessages/<UserId>')
def ReceiveMessages(UserId):
    # TODO
    return render_template("mainPage.html", count_books=count) 

############### Bots endpoints ####################
###################################################

# Sends messages to the user from a given bot in a certain building 
@app.route('/API/Bots/SendMessages/<BuildingId>')
def ReceiveMessages(BuildingId):
    # TODO
    return render_template("mainPage.html", count_books=count) 


if __name__ == '__main__':
    app.run()
