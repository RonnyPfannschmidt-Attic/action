from collections import deque
class Actor(object):

    def handle(self, message):
        raise NotImplementedError


class Null(Actor):
    def handle(self, message):
        return


class QueueActor(Actor):
    def __init__(self):
        self.items = deque()

    def handle(self, message):
        action, payload = message.data
        if action == 'put':
            self.items.append(payload)
            return []
        elif action == 'get':
            if self.items:
                return [
                    message.reply(('item', self.items.popleft()))
                ]
            else:
                return [
                    message.reply(('empty', None))
                ]

        assert 0





