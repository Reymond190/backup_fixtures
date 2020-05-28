import txredisapi as redis

from twisted.internet import defer
from twisted.internet import reactor


@defer.inlineCallbacks
def main():
    print('insid main')
    rc = yield redis.Connection()
    print (rc)

    v = yield rc.get("foo")
    print ("foo:", repr(v))

    yield rc.disconnect()
    print('disconnect'
    )


if __name__ == "__main__":
    main().addCallback(lambda ign: reactor.stop())
    print('aftercallback')
    reactor.run()