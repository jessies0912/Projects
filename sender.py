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


class sender:

    RTT = 20

    def isCorrupted(self, packet):
        '''This function determines if a received packet (acknowledgement) was corrupted during transmission.
            If the calculated checksum differs from the packet checksum, return true.
        '''
        temp = checksumCalc(packet.payload) + \
            packet.ackNum + packet.seqNum
        # using a temp variable to check if it equals the packet checksum and
        # if it does the reult is true
        if temp != (packet.checksum):
            diff = True

        else:
            diff = False
        # return statement
        return diff

    def isDuplicate(self, packet):
        '''determines if an acknowledgement packet is identical to or different from the equivalent function on the recipient side.
        '''
        if packet.ackNum == self.current_sequence_num:
            same = False
        else:
            same = True
            # duplicate error statement
            print("UH OH: RECEIVED duplicate AcK")
        # return statement
        return same

    def getNextSeqNum(self):
        '''generate the next sequence number to be used.
        '''

        if self.current_sequence_num == 0:
            self.current_sequence_num = 1
        else:
            self.current_sequence_num = 0
        # return statement
        return

    def __init__(self, entityName, ns):
        self.entity = entityName
        self.networkSimulator = ns
        print("Initializing sender: A: " + str(self.entity))

    def init(self):
        '''Set the sequence number and the packet in transit to their default values.
            There is no packet in transit at first, thus it should be set to None.
        '''
        self.currPacket = None
        self.current_sequence_num = 0
        # return statement
        return

    def timerInterrupt(self):
        '''In the event of a timer interrupt, this method emulates what the sender performs.
        This method resends the packet, resets the timer, and increases the timeout to twice the RTT.
        This function is never used. The simulator initiates it.
        '''
        self.networkSimulator.startTimer(self.entity, self.RTT * 2)
        self.networkSimulator.udtSend(self.entity, self.currPacket)
        # return statement
        return

    def output(self, message):
        '''prepare a packet and send the packet through the network layer
        by calling calling utdSend.
        It also start the timer.
        It must ignore the message if there is one packet in transit
        '''

        if self.currPacket == None:

            packet = Packet(self.current_sequence_num, self.current_sequence_num, checksumCalc(
                message.data) + (self.current_sequence_num * 2), message.data)
            # multiplying the sqence number by 2
            self.currPacket = packet  # setting the packet to current packet
            self.networkSimulator.startTimer(self.entity, self.RTT)
            self.networkSimulator.udtSend(self.entity, packet)

        # return statement

        return

    def input(self, packet):
        '''If the acknowlegement packet isn't corrupted or same, 
        transmission is complete. Therefore, indicate there is no packet
        in transition.
        The timer should be stopped, and sequence number  should be updated.

        In the case of same or corrupt acknowlegement packet, it does 
        not do anything and the packet will be sent again since the
        timer will be expired and timerInterrupt will be called by the simulator.
        '''

        if self.isCorrupted(packet) == False and self.isDuplicate(packet) == False:

            self.networkSimulator.stopTimer(self.entity)
            # currpacket == 0
            self.currPacket = None
            self.getNextSeqNum()
            self.networkSimulator.receiver.getNextExpectedSeqNum()
            # return statement
        return
