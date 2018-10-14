# -*- coding: utf-8 -*-

import messages_pb2
import os.path
from optparse import OptionParser

def sendMessage():
    print('Packaging message')
    message = messages_pb2.UpdateSignal()
    
    staResults = message.staresults.add()
    linkMeasurement = staResults.linkmeasurements.add()
    linkMeasurement.BSSID = 0x112233445566
    linkMeasurement.rssi = -55
    linkMeasurement = staResults.linkmeasurements.add()
    linkMeasurement.BSSID = 0x223344556688
    linkMeasurement.rssi = -75
    staResults.StaMAC = 0x1234567890ab
    
    message.BSSID = 0x112233445566
    print('-> from BSSID : ' + str(hex(message.BSSID)))
    
    return message.SerializeToString()
    
def receiveMessage(packedMessage):
    print('Receiving message')
    message = messages_pb2.UpdateSignal()
    
    message.ParseFromString(packedMessage)
    message.BSSID
    print('-> from BSSID : ' + str(hex(message.BSSID)))
    
    for staResults in message.staresults:
        print('--> Client MAC: ' + str(hex(staResults.StaMAC)))
        
        for linkMeasurement in staResults.linkmeasurements:
            print('---> Saw BSSID: ' + str(hex(linkMeasurement.BSSID)) + ' at ' + str(linkMeasurement.rssi) + ' dB')
            
def writeBinaryDataToFile(binaryData, filename):
    with open(os.getcwd() + "/" + filename, 'wb') as outputFile:
        print('-> Writing to: ' + filename)
        outputFile.write(binaryData)
        
def readBinaryDataFromFile(filename):
    with open(os.getcwd() + "/" + filename, 'rb') as inputFile:
        print('-> Reading from: ' + filename)
        binaryData = inputFile.read()
        
    return binaryData

def main(options):
    print('Base line protobuf send/receive test, V1')
    print('----------------------------------------')
    
    if (options.mode == "1"):
        print('Mode 1 - direct memory transfer.')
        packedMessage = sendMessage()
        receiveMessage(packedMessage)
    
    if (options.mode == "2"):
        print('Mode 2 - transfer via intermediate file.')
        print('-> File: ' + options.filename)
        packedMessage = sendMessage()
        writeBinaryDataToFile(packedMessage, options.filename)
        readMessage = readBinaryDataFromFile(options.filename)
        receiveMessage(readMessage)
    
    if (options.mode == "3"):
        print('Mode 3 - read existing file.')
        print('-> File: ' + options.filename)
        if (os.path.exists(options.filename)):
            readMessage = readBinaryDataFromFile(options.filename)
            receiveMessage(readMessage)
        else:
            print('Could not find specified file!')
    
    print('----------------------------------------')
    
if __name__ == "__main__":
   parser = OptionParser()
   
   parser.add_option("-f", "--file", dest="filename",
                     help="use this file to read from / write to.", metavar="FILE",
                     default="message_v1.bin")	
   parser.add_option("-m", "--mode", dest="mode",
                     help="test mode: 1 = direct, 2 = via file, 3 = only FROM file.", metavar="MODE",
                     default="1")
   
   (options, args) = parser.parse_args()
   main(options)

    