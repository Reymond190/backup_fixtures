#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import txredisapi as redis

### Protocol Implementation

# This is just about the simplest possible protocol
class Echo(Protocol):

    def connectionMade(self):
        print(self.transport.getPeer())

    def dataReceived(self, data):
        """
        As soon as any data is received, write it back.
        """
        self.transport.write(data)
        print(self.transport.getPeer())
        print(data)

    def connectionLost(self, reason):
        print(reason)


def main():
    rc = redis.Connection()
    print(rc)
    rc.set("foo", "bar")
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    reactor.run()
    print(rc.get("foo"))
    rc.disconnect()

if __name__ == '__main__':
    main()
