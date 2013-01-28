class Actor(object):

    def handle(self, message):
        raise NotImplementedError


class Null(Actor):
    def handle(self, message):
        return

