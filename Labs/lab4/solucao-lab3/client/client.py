#!/usr/bin/env python

import Pyro4
import dbUI

# Diz ao Pyro para usar o pickle como seriador
Pyro4.config.SERIALIZER = 'pickle'

def main():
	#Looks for the name server
        ns = Pyro4.locateNS()
        #Looks for the object BookBD in the nameserver
        uri = ns.lookup('BookDB')
        
        #Creates a proxy (with Pyro, your remote method calls on Pyro objects go though a proxy)
        db = Pyro4.Proxy(uri)

        
        ui = dbUI.dbUI(db)
        ui.menu()

if __name__=="__main__":
        main() 
