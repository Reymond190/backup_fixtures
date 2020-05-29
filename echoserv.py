#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import sys

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import txredisapi as redis
import redis
from twisted.internet import defer
from twisted.protocols.basic import LineReceiver

### Protocol Implementation

# This is just about the simplest possible protocol

def helo(data):
    asd = str(data)
    for i in asd:
        print(i)
    return asd



class Echo(Protocol):

    def connectionMade(self):
        print(self.transport.getPeer())

    def dataReceived(self, data):
        """
        As soon as any data is received, write it back.
        """


        print('sdfjskdfjlskjd')



        self.transport.write('null'.encode())
        print(self.transport.getPeer())
        print(data)

    def connectionLost(self, reason):
        print(reason)


def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8888, f)
    reactor.run()

if __name__ == '__main__':
    main()
