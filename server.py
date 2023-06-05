import socket


localIP = "192.168.0.114"

localPort = 3400 # Change to server port

bufferSize = 1024


msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)


# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))


print("UDP server up and listening")


# Listen for incoming datagrams

while (True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)


# Takes object location, direction of movement, and Velocity
def calculate_loco(object_loc, dir, v):
    print('test')

# Takes object location, area of movement (a), velocity, and optional variable m
def collison_detect(obj_loc,a,v,m):
    print('test detect')