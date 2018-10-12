# -*- coding: utf-8 -*-

import messages_pb2

def sendMessage():
    print('Packaging message')
    message = messages_pb2.UpdateSignal()
    
    staResults = message.staresults.add()
    linkMeasurement = staResults.linkmeasurements.add()
    linkMeasurement.BSSID = 18838586676582 # 0x112233445566ULL
    linkMeasurement.rssi = -55
    linkMeasurement = staResults.linkmeasurements.add()
    linkMeasurement.BSSID = 37603585123976 # 0x223344556688ULL
    linkMeasurement.rssi = -75
    staResults.StaMAC = 20015998341291 # 0x1234567890abULL
    
    message.BSSID = 18838586676582 # 0x112233445566ULL # Can be used directly...
    print('-> from BSSID : ' + str(message.BSSID))     # ... but does not print nicely.
    
    return message.SerializeToString()
    
def receiveMessage(packedMessage):
    print('Receiving message')
    message = messages_pb2.UpdateSignal()
    
    message.ParseFromString(packedMessage)
    message.BSSID
    print('-> from BSSID : ' + str(message.BSSID))
    
    for staResults in message.staresults:
        print('--> Client MAC: ' + str(staResults.StaMAC))
        
        for linkMeasurement in staResults.linkmeasurements:
            print('---> Saw BSSID: ' + str(linkMeasurement.BSSID) + ' at ' + str(linkMeasurement.rssi) + ' dB')

if __name__ == "__main__":
    print('Base line protobuf send/receive test')
    print('----------------------------------------')
    packedMessage = sendMessage()
    print('      |\n      v')
    receiveMessage(packedMessage)
    print('----------------------------------------')
    