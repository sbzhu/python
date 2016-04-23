#!/usr/bin/python
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)

serverName = '10.136.64.114'; serverPort = 12000

while(1):
	message = raw_input('Input lowercase sentence : ')
	clientSocket.sendto(message, (serverName, serverPort))

	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage

clientSocket.close()
