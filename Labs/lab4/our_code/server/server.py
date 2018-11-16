#!/usr/bin/env python

import Pyro4
import bookDB




Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

def main():
        remoteLibrary = Pyro4.expose(bookDB.bookDB)

        db = bookDB.bookDB("mylib")
        db2 = bookDB.bookDB("mylib")


        daemon = Pyro4.Daemon()

        ns = Pyro4.locateNS()
        print (ns)

        try:
                ns.createGroup(':libraries')
        except:
                pass

        uri1 = daemon.register(db, "DB1")
        uri2 = daemon.register(db2, "BDB2")

        ns.register("BookDB-81232A", uri1)
        ns.register("BookDB-81232B", uri2)

        try:
                daemon.requestLoop()
        finally:
                daemon.shutdown(True)

if __name__=="__main__":
        main() 
