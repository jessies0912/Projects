"""
-------------------------------------------------------
[A2: Developing a dependable transport protocol. 
Observing in action how a dependable transport system such as TCP operates]
-------------------------------------------------------
Author:  Jasmeet Salh & Muhammad Farzan Ali
ID:      190770960 & 191651560
Email:   salh0960@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""
# Imports

# Constants

from common import *


class receiver:

    def isCorrupted(self, packet):
        ''' Checks if a packet received during transmission has been corrupted.
    If the checksum computed differs from the checksum in the packet, return true.'''

        chcksum_computed = checksumCalc(
            packet.payload) + packet.ackNum + packet.seqNum

        if chcksum_computed == (packet.checksum):
            crpt = False
        else:
            crpt = True
        # return statement
        return crpt

    def isDuplicate(self, packet):
        '''determines if the packet sequence number matches the intended sequence number'''
        if self.expected_seqNum == packet.seqNum:
            same = False
        else:
            same = True
        # return statement
        return same

    def getNextExpectedSeqNum(self):
        '''The expected sequence numbers are 0 or 1'''
        if self.expected_seqNum == 0:
            self.expected_seqNum = 1
        else:
            self.expected_seqNum = 0
        # return statement
        return

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing receiver: B: " + str(self.entity))

    def init(self):
        '''initialize expected sequence number'''
        self.expected_seqNum = 0
        # return statement
        return

    def input(self, packet):
        '''When a packet sent from the sender arrives at the receiver, 
        this method will be invoked. It sends a packet with the ack number equal 
        to the sequence number of the previous successfully received packet if the received 
        packet is malformed or duplicate. You can utilise the sequence number that isn't expected 
        because there are only 0 and 1 sequence numbers.

        If packet is OK (not a duplicate or corrupted), deliver it to the
        application layer and send an acknowledgement to the sender
        '''

        if (self.isCorrupted(packet) == False and self.isDuplicate(packet) == False):
            self.networkSimulator.udtSend(self.entity, packet)
            self.networkSimulator.deliverData(self.entity, packet)
        # return statement
        return
