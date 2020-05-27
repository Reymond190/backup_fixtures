from twisted.internet import reactor, protocol
from twisted.protocols.memcache import MemCacheProtocol, DEFAULT_PORT
d = protocol.ClientCreator(reactor, MemCacheProtocol
        ).connectTCP("localhost", DEFAULT_PORT)
def doSomething(proto):
    # Here you call the memcache operations
    print('do something')
    return proto.set("mykey", "a lot of data")

d.addCallback(doSomething)
reactor.run()