# IMPORTS
from random import randint, choice
import struct
import time
from socket import *
import sys

# The client sends a packet to the server, which the server receives, validates, and answers with a formatted packet.
# Assigning client to 1 and Server to 2
CLIENT = 1
SERVER = 2
pcode = 0

# Declaring the port num
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Binding the socket
serverSocket.bind(("localhost", serverPort))

while True:
    print('\nReady to receive')

    # clientaddress is recieved once first packet sent
    sentence, clientAddress = serverSocket.recvfrom(1024)
    data_len, pcode, entity, data = struct.unpack("!IHHs", sentence[:9])

    print("receiving from the client: data_len: {0}, pcode: {1}, entity: {2}, sentence: {3}".format(
        data_len, pcode, entity, sentence.decode()))

    print("\n------------ Starting Stage A  ------------")
    # data_len = len(sentence)

    # print("Server is sending capitalized sentence to client")

    # serverSocket.sendto(capitalizedSentence.encode(), clientAddress)

    print("Initializing variables for repeat, udp_port, ln, & codeA")
    repeat = randint(5, 20)
    udp_port = randint(20000, 30000)
    ln = randint(50, 100)
    codeA = randint(100, 400)

    # print("Creating packet with data_len, pcode, entity, repeat, udp_port, ln, codeA")
    entity = SERVER
    data_len = len(struct.pack("!IIHH", repeat, udp_port, ln, codeA))

    print("Sending to the client - data_len: {0}, pcode: {1}, entity: {2}, repeat: {3}, Udp_port: {4}, len: {5}, codeA: {6}".format(
        data_len, pcode, SERVER, repeat, udp_port, ln, codeA))

    print(data_len)
    packet = struct.pack("!IHHIIHH",  data_len, pcode,
                         entity, repeat, udp_port, ln, codeA)

    serverSocket.sendto(packet, clientAddress)
    # print("Packet is sent")
    serverSocket.close()
    print("SERVER:------------ End of Stage A  ------------\n")

    print('SERVER:------------ Starting Stage B  ------------ The server is ready to receive for phase B----')
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(("localhost", udp_port))
    print("Server is now listening on udp_port: ", udp_port)
    packet_size = len(struct.pack("IHH", data_len, pcode, entity))
    print("packet_size", packet_size)

    packets_recieved = 0
    while(packets_recieved < repeat):
        serverSocket.settimeout(3)
        clientResponse, clientAddress = serverSocket.recvfrom(2048)
        # TODO Verify packets
        data_len, pcode, entity, packet_id = struct.unpack(
            "!IHHI", clientResponse[:12])
        print(
            f'SERVER: received_packet_id = {packet_id} data_len =  {data_len}  pcode: {pcode} entity: {entity}')

        serverMessage = struct.pack(
            "!IHHI", data_len, pcode, SERVER, packets_recieved)
        serverSocket.sendto(serverMessage, clientAddress)
        packets_recieved += 1

    print("------------- B2: -------------")
    tcp_port = randint(20000, 30000)
    codeB = randint(100, 400)
    packet = struct.pack(
        '!IHHII', data_len, pcode, SERVER, tcp_port, codeB)
    serverSocket.sendto(packet, clientAddress)
    print(
        f'Sending to the client - data_len: {data_len} pcode: {pcode} entity: {SERVER} tcp_port {tcp_port} codeB {codeB}')

    print("------------ End of Stage B  ------------")
    serverSocket.settimeout(2)

    serverSocket.close()

    print("\n------------ Starting Stage C  ------------")
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("localhost", tcp_port))
    serverSocket.listen(1)
    print("Server is now listening on tcp port: ", tcp_port)
    # connectionAddr = serverSocket.accept()
    # time.sleep(1)
    connectionSocket, addr = serverSocket.accept()
    print("Conn. Accepted")
    repeat2 = randint(5, 20)
    len2 = randint(50, 100)
    codeC = randint(100, 400)
    char = choice('abcdefghijklmnopqrstuvwyxz'.upper()).encode('utf-8')

    packet = struct.pack("!IHHIIIc", data_len, pcode,
                         entity, repeat2, len2, codeC, char)
    connectionSocket.send(packet)
    print("Server sending to client: data_length = {0}, pcode = {1}, entity = {2}, repeat2 = {3}, len2 = {4}, codeC = {5}, char = {6}".format(
        data_len, pcode, entity, repeat2, len2, codeC, char.decode()))
    # print("Sent packet to client - data_len: " + str(data_len) + ", pcode/codeB: " + str(pcode) + ", entity: " + str(entity)
    #       + ", len2: " + str(len2) + ", codeC: " + str(codeC) + ", char: " + str(char))
    print("------------ End of Stage C  ------------\n------------ Starting Stage D  ------------")

    serverSocket.listen(1)
    rec_packet = 0
    print("Now listening for packets from Client")
    while(rec_packet < repeat2):
        connectionSocket.settimeout(3)  # The server does not listen for 3 secs
        rec = connectionSocket.recv(1024)
        data_len, pcode, entity = struct.unpack('!IHH', rec[:8])
        connectionSocket.settimeout(3)
        print("recieved_packet = {0}, data_len = {1}, pcode = {2}, entity = {3}, data = {4}".format(
            rec_packet, data_len, pcode, entity, rec[8:].decode()))
        rec_packet += 1

    codeD = randint(100, 400)
    serverMessage = struct.pack("!IHHI", data_len, pcode, SERVER, codeD)
    print("Sending packet back to client.")
    connectionSocket.send(serverMessage)
    connectionSocket.close()  # Closing the connectionSocket
    sys.exit()  # Exit the program
