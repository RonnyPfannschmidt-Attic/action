from collections import deque



class InstanceDispatcher(object):
    def __init__(self, dispatcher, instance):
        self.instance = instance
        self.dispatcher = dispatcher

    def __call__(self, message):
        class_ = type(message)




class Dispatcher(object):
    def __get__(self, instance, class):
        return InstanceDispatcher(instance, self)


class Actor(object):
    def handle(self, message):
        raise NotImplementedError


class Null(Actor):
    def handle(self, message):
        return []





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
