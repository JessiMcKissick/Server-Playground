import socket

# Goal: Have servers add live server number to a file
# The server gate gets how many servers are live on an interval
# When a client initially connects the gate checks each active server sequentially and connects the client to
# the lowest utilization server.
# If no active servers are available or all active servers are at 80+ percent utilization the gate will spin up a new
# server (up to a pre-set number of allowed servers.)

# Gate checks active list, sends port of open server back to the client with the specific servers activation key,
# the client then closes the connection to the gate and connects to the selected server.

# The activation key is effectively a server password to prevent joining a specific server via hacking / modding
# Activation keys are re-rolled every x amount of hours. After logging out, the server will save the players uuid
# for a few hours so the player can rejoin the server at will (unless its full at which point the gate will send
# them to a new server instead)

# Players need to be able to join their friends so in-game function should exist to join friend at which point the 
# the friends client will send the server key to the joining friends client and the joining friend will send a 
# join request to the gate with the key included. If the server is full the game will just say no and send them to
# a new server.


# Come to think there need to be 2 different server types: Universe and ship. Universe servers need to be able to 
# handle massive amounts of work simultaneously as it's the server where /everyone/ thats playing is connected 
# simultaneously... So the universe server needs to handle very simple data like ship movement and basic actions

# ship servers only really need to handle ship stuff. Player movement, collision data from the client, enemy movement,
# etc. These servers can multitask but don't need to be universal so one server could handle a few hundred ships or
# so. Requires some testing in the future.

# Planet servers (maybe, not sure if this'll be a feature) need to be in the middle. They need to handle everyone
# on the planet at once. Maybe have a planet server handle the communication and have slave servers handle all the 
# work on more complex actions.

# For early tests however it's all on my home server so small player groups at best. Server system should really only 
# take up at most 60% of the server at this scale (it's not a powerful rig)

localIP = "192.168.0.114"

localPort = 3400  # Change to server port

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


def collison_detect(obj_loc, a, v, m):
    print('test detect')
