import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Client
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print( 'connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:
    while True:
        # Send data
        print("Enter one of the following comands: push, pop, add, sum")


        message = input(">> ")
        print( 'sending "%s"' % message, file = sys.stderr)
        sock.sendall(message.encode('utf-8'))

        if(message == "push"):
            print("Enter a number to be pushed")
            num = input(">> ")
            time.sleep(0.3)
            sock.sendall(num.encode('utf-8'))

        
    
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        #while amount_received < 0:
        data = sock.recv(100)
        #amount_received += len(data)
        print( 'received "%s"' % data, file=sys.stderr)

finally:
    print( 'closing socket', sys.stderr)
    sock.close()
