#!/usr/bin/env python

import Pyro4
import dbUI
import random
class multi_proxy:
        multiproxy_list = []
        uri=[]

        def __init__(self, ns_ip, ns_port):

                #ns = Pyro4.locateNS(ns_ip, ns_port)
                ns = Pyro4.locateNS()
                list_server = ns.list(prefix="BookDB")
                i=0
                
                #print (list_server)
                for server in list_server:
                        uri = ns.lookup(server)
                        self.multiproxy_list.append(Pyro4.Proxy(uri))  
                        i=i+1
                        
        def addBook(self, author, title, year):
                db = random.choice(self.multiproxy_list)
                db.addBook(author, title, year)


        def showBook(self, b_id):
                listallbooks = []
                for proxy in self.multiproxy_list:
                        listallbooks= proxy.listAllBooks()  
                for book in listallbooks:
                        if(book.id== b_id):
                                return book


        def listAllBooks(self):
                allbooksbib=[]
                for proxy in self.multiproxy_list:
                        allbooksbib= allbooksbib+(proxy.listAllBooks())
                        
                return (allbooksbib)

        def listBooksAuthor(self, authorName):
                ret_value = []
                for proxy in self.multiproxy_list:
                        for b in proxy.listAllBooks():
                                if b.author == authorName:
                                        ret_value.append(b)
                return ret_value

        def listBooksYear(self, year):
                ret_value = []
                for proxy in self.multiproxy_list:
                        for b in proxy.listAllBooks():
                                if b.year == year:
                                        ret_value.append( b)
                return ret_value
                       

                #self.ns_random = random.choice(list_server)

                




Pyro4.config.SERIALIZER = 'pickle'

def main():
      
        #db2 = Pyro4.Proxy(uri2)
        #multi_proxy1 = multi_proxy("193.136.128.109" , 9090)
        multi_proxy1 = multi_proxy("193.136.128.109" , 9090)
        
        ui = dbUI.dbUI(multi_proxy1)
        ui.menu()

if __name__=="__main__":
        main() 
