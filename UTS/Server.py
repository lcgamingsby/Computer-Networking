# import socket module
from socket import *
import sys  # In order to terminate the program

# Define server parameters
serverPort = 6789
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start and end

    try:
        # Receive the client request message
        message = connectionSocket.recv(1024).decode()  # Fill in start and end
        print("Message received:", message)

        # Extract the requested filename from the message
        filename = message.split()[1]
        f = open(filename[1:])  # [1:] to remove the leading "/"

        # Read the file content
        outputdata = f.read()  # Fill in start and end

        # Send HTTP header line into the socket for a successful response
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())  # Fill in start and end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())  # Send a new line after the content

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()

# Close the server socket (although we won’t reach here in this simple loop)
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
