# -*- coding: utf-8 -*-

import messages2_pb2
import os.path
from optparse import OptionParser

def sendMessage():
    print('Packaging message')
    message = messages2_pb2.UpdateSignal()
    
    staResults = message.staresults.add()
    linkMeasurement = staResults.linkmeasurements.add()
    linkMeasurement.BSSID = 18838586676582 # 0x112233445566ULL
    linkMeasurement.rssi = -55
    linkMeasurement.snr = 20 # New in V2
    linkMeasurement = staResults.linkmeasurements.add()
    linkMeasurement.BSSID = 37603585123976 # 0x223344556688ULL
    linkMeasurement.rssi = -75
    linkMeasurement.snr = 25 # New in V2
    staResults.StaMAC = 20015998341291 # 0x1234567890abULL
    
    message.BSSID = 18838586676582 # 0x112233445566ULL # Can be used directly...
    print('-> from BSSID : ' + str(message.BSSID))     # ... but does not print nicely.
    
    return message.SerializeToString()
    
def receiveMessage(packedMessage):
    print('Receiving message')
    message = messages2_pb2.UpdateSignal()
    
    message.ParseFromString(packedMessage)
    message.BSSID
    print('-> from BSSID : ' + str(message.BSSID))
    
    for staResults in message.staresults:
        print('--> Client MAC: ' + str(staResults.StaMAC))
        
        for linkMeasurement in staResults.linkmeasurements:
            snrValueText = ''
            # Handle the optional new field that appeared in protocol V2
            if (linkMeasurement.snr != 0):
                snrValueText = ' with SNR = ' + str(linkMeasurement.snr)
            print('---> Saw BSSID: ' + str(linkMeasurement.BSSID) + ' at ' + str(linkMeasurement.rssi) + ' dB' + snrValueText)
            
            
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
    print('Base line protobuf send/receive test, V2')
    print('------------------------------------------------------')
    
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
    
    print('------------------------------------------------------')
    
if __name__ == "__main__":
   parser = OptionParser()
   
   parser.add_option("-f", "--file", dest="filename",
                     help="use this file to read from / write to.", metavar="FILE",
                     default="message_v2.bin")	
   parser.add_option("-m", "--mode", dest="mode",
                     help="test mode: 1 = direct, 2 = via file, 3 = only FROM file.", metavar="MODE",
                     default="1")
   
   (options, args) = parser.parse_args()
   main(options)

    