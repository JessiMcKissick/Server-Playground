import socket


msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

# Change to server IP and selected port
serverAddressPort = ("174.134.32.154", 3400)

bufferSize = 1024


# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


# Send to server using created UDP socket
while(True):

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


    msgFromServer = UDPClientSocket.recvfrom(bufferSize)


    msg = "Message from Server {}".format(msgFromServer[0])

    print(msg)
