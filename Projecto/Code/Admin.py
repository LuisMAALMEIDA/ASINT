import requests
import json





def DefineBuilding():
    l = input('Insert the id, name, latitude, longitude and radius separated by # :\n')
    # pline -> processed line
    pline = l.split('#')
    if len(pline) ==5:
        print ('%s %s %s'% (pline[0], pline[1], pline[2]))
        # Sends the building feature to the server
        payload = {'ID': pline[0] , 'Name': pline[1] , 'Latitude':pline[2], 'Longitude': pline[3], 'Radius': pline[4] }
        r = requests.post("http://127.0.0.1:5000/API/Admin/CreateBuilding", json=payload)
        data = r.json()
        json_acceptable_string = data.replace("'", "\"")
        msg = json.loads(json_acceptable_string)
        print(msg["Msg"])
    else:
        print('Error in defining a building')



def ListAllUsersSystem():
    r = requests.post("http://127.0.0.1:5000/API/Admin/ListUsers")
    data = r.json()
    json_acceptable_string = data.replace("'", "\"")
    users = json.loads(json_acceptable_string)

    for user in users:
        if "Name" in user:
                print("Name:"+user["Name"]+", IstID:" + str(user["IstID"])+", Range:" + str(user["Range"]) )
        else:
                # As Name it's not a key from users, then there are no users on the server
                print("Non user is logged in")
    



def ListUsrInBuiliding():
    l = input('Insert a building ID :\n')
    # TODO
    url="http://127.0.0.1:5000/API/Admin/ListUsers/"+l
    r = requests.post(url)
    data = r.json()
    json_acceptable_string = data.replace("'", "\"")
    users = json.loads(json_acceptable_string)  
    for user in users:
        if "Name" in user:
                print("Name:"+user["Name"]+", IstID:" + user["IstID"]+", Range:" + user["Range"] )
        else:
                print("Non user is the builing in")
    



# List the history of all users movementes and exanged messages by user
def HistoryUsers():
    l = input('Insert the user ID :\n')

    url="http://127.0.0.1:5000/API/Admin/Logs/User/"+l
    r = requests.post(url)
    data = r.json()
    json_acceptable_string = data.replace("'", "\"")
    dic_book = json.loads(json_acceptable_string)       
    # TODO ver o que é o print faz, i dont remember
    print(dic_book)


# List the history of all users movementes and exanged messages by building
def HistoryBuilding():
    l = input('Insert the Building ID :\n')

    url="http://127.0.0.1:5000/API/Admin/Logs/BuildingID/"+l
    r = requests.post(url)
    data = r.json()
    json_acceptable_string = data.replace("'", "\"")
    dic_book = json.loads(json_acceptable_string)       
    # TODO ver o que é o print faz, i dont remember
    print(dic_book)




def main():
            
    exit = False
    while not exit:
        print('Menu:')
        print('1- Define building\n2- List all users that are logged in the system')
        print('3- List all users that are inside a certain building')
        print('4- List the history of all users movementes and exanged messages by user')
        print('5- List the history of all users movementes and exanged messages by building')
        print('6- to quit')
        l = input(">>")
        l = l.split()

        if len(l)==1:
                
                command = ''.join(l)
                
                #Quit
                if command=='6':
                        exit = True

                # Define buiding
                elif command == '1':
                    DefineBuilding()

                #List all users in the system
                elif command == '2':
                       ListAllUsersSystem()
                #List all users inside a certain build
                elif command == '3':
                        ListUsrInBuiliding()

                elif command == '4':
                        HistoryUsers()       
                elif command == '5':
                        HistoryBuilding()
        






if __name__=="__main__":
        main() 