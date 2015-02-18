from collections import namedtuple, deque

MessageBase = namedtuple('Message', [
    'target', 'source', 'data',
])





class Message(MessageBase):
    def reply(self, data):
        return Message(target=self.source, source=self.target, data=data)


class MessageQueue(object):

    def __init__(self):
        self.messages = deque()

    def put(self, message):
        self.messages.append(message)

    def dispatch_one(self):
        message = self.messages.popleft()
        new_messages = message.target.handle(message)
        self.messages.extend(new_messages)

    def run(self):
        while self.messages:
            self.dispatch_one()

