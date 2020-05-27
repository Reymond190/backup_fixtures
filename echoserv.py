#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import txredisapi as redis

from twisted.internet import defer

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

@defer.inlineCallbacks
def main():
    rc = yield redis.Connection()
    print(rc)
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    yield rc.set("foo", "bar")
    v = yield rc.get("foo")
    print(v)
    reactor.run()

if __name__ == '__main__':
    main()
