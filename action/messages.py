from collections import namedtuple, deque

Message = namedtuple('Message', [
    'target', 'source', 'data',
])

class MessageQueue(object):

    def __init__(self):
        self.messages = deque()

    def put(self, message):
        self.messages.append(message)

    def run_once(self):

        message = self.messages.popleft()
        message.target.handle(message)


