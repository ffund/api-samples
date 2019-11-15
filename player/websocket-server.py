#!/usr/bin/python

from twisted.internet import protocol, reactor
from txws import WebSocketFactory
import socket

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        #global s
        print data
        #s.send(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

#global s 
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("witestlab.poly.edu", 3003))

reactor.listenTCP(9080, WebSocketFactory(EchoFactory()))
reactor.run()

