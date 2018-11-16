#!/usr/bin/env python

import Pyro4
import dbUI
import random
import requests
import json

class proxy:
      



                        
        def addBook(self, author, title, year):
                
                payload = {'Author': author , 'Title': title , 'Year': year }
                r = requests.post("http://127.0.0.1:5000/API/addBook", json=payload)
                #r = requests.post("http://127.0.0.1:5000/API/addBook", data=json.dumps(payload))
                print(r.text)
                


        def showBook(self, b_id):
                listallbooks = []
                for proxy in self.multiproxy_list:
                        listallbooks= proxy.listAllBooks()  
                for book in listallbooks:
                        if(book.id== b_id):
                                return book


        def listAllBooks(self):

                r = requests.get( "http://127.0.0.1:5000/API/Books")
                print(r.status_code)
                data = r.json()
                json_acceptable_string = data.replace("'", "\"")
                dic_book = json.loads(json_acceptable_string)
                return dic_book
                
                        


        def listBooksAuthor(self, authorName):
                payload = {'Author': authorName}
                #Manda o nome do author para o endpoint indicado pelo URI
                r = requests.post("http://127.0.0.1:5000/API/listBooksAuthor", json=payload)
                print(r.status_code)
                data = r.json()
                json_acceptable_string = data.replace("'", "\"")
                dic_book = json.loads(json_acceptable_string)
                return dic_book

        def listBooksYear(self, year):
                ret_value = []
                for proxy in self.multiproxy_list:
                        for b in proxy.listAllBooks():
                                if b.year == year:
                                        ret_value.append( b)
                return ret_value
                       

                #self.ns_random = random.choice(list_server) """

                




Pyro4.config.SERIALIZER = 'pickle'

def main():
            
    proxy1 = proxy() 
    ui = dbUI.dbUI(proxy1)
    ui.menu()
    



if __name__=="__main__":
        main() 