#!/usr/bin/python
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)

hostName = ''; serverPort = 12000
serverSocket.bind((hostName, serverPort))
print 'The server is ready to receive'

while(1) : 
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)

