# -*- coding: utf-8 -*-

# JSON encoded message example:
#
# "signalUpdate" : {
#   "bssid" : "11:22:33:44:55:66",
#   "staResults" : {
#     "12:34:56:78:90:ab" : {
#       "accessPoints" : {
#         "11:22:33:44:55:66" : {
#           "rssi" : -55
#         },
#         "22:33:44:55:66:77" : {
#            "rssi" : -75
#         }
#       }
#     }
#   }
# }

import json
import os.path
from optparse import OptionParser

def sendMessage():
    print('Packaging message')
    message = {}
    signalUpdate = {}
    
    linkMeasurements = {"11:22:33:44:55:66" : { "rssi" : -55 }, "22:33:44:55:66:77" : { "rssi" : -75 } }
    
    staResults = {"12:34:56:78:90:ab" : { "accessPoints" : linkMeasurements } }

    signalUpdate["bssid"] = "11:22:33:44:55:66"    
    signalUpdate["staResults"] = staResults
    
    message["signalUpdate"] = signalUpdate
    
    print('-> from BSSID : ' + signalUpdate["bssid"])
    
    return json.dumps(message)
    
def receiveMessage(packedMessage):
    print('Receiving message')
    message = json.loads(packedMessage)
    
    signalUpdate = message["signalUpdate"]
    print('-> from BSSID : ' + signalUpdate["bssid"])
    
    for staResults_bssid in signalUpdate["staResults"].keys():
        print('--> Client MAC: ' + staResults_bssid)        
        linkMeasurements = signalUpdate["staResults"][staResults_bssid]["accessPoints"]
        
        for measurement_bssid in linkMeasurements.keys():
            measurementItems = linkMeasurements[measurement_bssid]
            print('---> Saw BSSID: ' + measurement_bssid + ' at ' + str(measurementItems["rssi"]) + ' dB')
            
def writeJSONDataToFile(stringData, filename):
    with open(os.getcwd() + "/" + filename, 'w') as outputFile:
        print('-> Writing to: ' + filename)
        outputFile.write(stringData)
        
def readJSONDataFromFile(filename):
    with open(os.getcwd() + "/" + filename, 'r') as inputFile:
        print('-> Reading from: ' + filename)
        stringData = inputFile.read()
        
    return stringData

def main(options):
    print('Base line protobuf send/receive test, Vx')
    print('------------------------------------------------------')
    
    if (options.mode == "1"):
        print('Mode 1 - direct memory transfer.')
        packedMessage = sendMessage()
        receiveMessage(packedMessage)
    
    if (options.mode == "2"):
        print('Mode 2 - transfer via intermediate file.')
        print('-> File: ' + options.filename)
        packedMessage = sendMessage()
        writeJSONDataToFile(packedMessage, options.filename)
        readMessage = readJSONDataFromFile(options.filename)
        receiveMessage(readMessage)
    
    if (options.mode == "3"):
        print('Mode 3 - read existing file.')
        print('-> File: ' + options.filename)
        if (os.path.exists(options.filename)):
            readMessage = readJSONDataFromFile(options.filename)
            receiveMessage(readMessage)
        else:
            print('Could not find specified file!')
    
    print('------------------------------------------------------')
    
if __name__ == "__main__":
   parser = OptionParser()
   
   parser.add_option("-f", "--file", dest="filename",
                     help="use this file to read from / write to.", metavar="FILE",
                     default="message_vx.json")	
   parser.add_option("-m", "--mode", dest="mode",
                     help="test mode: 1 = direct, 2 = via file, 3 = only FROM file.", metavar="MODE",
                     default="1")
   
   (options, args) = parser.parse_args()
   main(options)

    
