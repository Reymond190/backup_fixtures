

import txredisapi as redis

from twisted.internet import defer
from twisted.internet import reactor


def sleep(n):
    d = defer.Deferred()
    reactor.callLater(5, lambda *ign: d.callback(None))
    return d


@defer.inlineCallbacks
def main():
    rc = yield redis.ConnectionPool()
    print (rc)

    # set
    yield rc.set("foo", "bar")

    # sleep, so you can kill redis
    print ("sleeping for 5s, kill redis now...")
    yield sleep(5)

    try:
      v = yield rc.get("foo")
      print ("foo:", v)

      yield rc.disconnect()
    except redis.ConnectionError:
      print (str('gone workge'))


if __name__ == "__main__":
    main().addCallback(lambda ign: reactor.stop())
    reactor.run()