#!/usr/bin/env python

import Pyro4
import dbUI
import random
import requests
import json

class proxy:
      



                        
        def addBook(self, author, title, year):
                
                payload = {'Author': author , 'Title': title , 'Year': int(year) }
                r = requests.post("http://127.0.0.1:5000/API/addBook", json=payload)
                #r = requests.post("http://127.0.0.1:5000/API/addBook", data=json.dumps(payload))
                 #print(r.text)
                


        def showBook(self, b_id):
                payload = {'BookID': b_id}
                #Manda o nome do author para o endpoint indicado pelo URI
                r = requests.post("http://127.0.0.1:5000/API/showbook", json=payload)
                data = r.json()
                json_acceptable_string = data.replace("'", "\"")
                dic_book = json.loads(json_acceptable_string)
                return dic_book


        def listAllBooks(self):

                r = requests.get( "http://127.0.0.1:5000/API/Books")
                #print(r.status_code)
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
                payload = {'Year': year}
                r = requests.post("http://127.0.0.1:5000/API/listBooksYear", json=payload)
                print(r.status_code)
                data = r.json()
                json_acceptable_string = data.replace("'", "\"")
                dic_book = json.loads(json_acceptable_string)
                return dic_book
        # Lista todos os livros de um certo author num dado ano
        def booksbyauthorinyear(self, author, year):
                payload = {'Author' : author, 'Year': year}
                r = requests.post("http://127.0.0.1:5000/API/booksbyauthorinyear", json=payload)
                print(r.status_code)
                data = r.json()
                json_acceptable_string = data.replace("'", "\"")
                dic_book = json.loads(json_acceptable_string)
                return dic_book


                       

              




Pyro4.config.SERIALIZER = 'pickle'

def main():
            
    proxy1 = proxy() 
    ui = dbUI.dbUI(proxy1)
    ui.menu()
    



if __name__=="__main__":
        main() 