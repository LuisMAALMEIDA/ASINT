import socket
import sys
import ex1
#Server
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print( 'starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print( 'connection from', client_address, file=sys.stderr)
        stack1 =ex1.rpnCalculator()
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received "%s"' % data, file=sys.stderr )
            if data:
                print(data)

                #PUSH
                if(data==b'push'):                  
                    data1 = connection.recv(16)
                    print(data1)
                    stack1.pushValue(data1)
                    print( 'sending pushed value back to client %s '% data1,  file=sys.stderr)
                    connection.sendall(data1)

                # POP    
                if(data==b'pop'):
                    stack1.popValue()
                    print( 'i did a pop on a stack', file=sys.stderr)
                    data1="You did a pop on a stack"
                    connection.sendall(data1.encode('utf-8'))

                #ADD
                if(data==b'add'):                   
                    stack1.add()
                    print( 'sending pushed value back to client',  file=sys.stderr)
                    data1=stack1.stack[len(stack1.stack)-1]
                    
                    connection.sendall(str(data1).encode('utf-8'))     
                       
            else:
                print('no more data from', client_address, file=sys.stderr)
                break
            
    finally:
        # Clean up the connection
        connection.close()