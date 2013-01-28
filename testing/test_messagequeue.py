from action.messages import MessageQueue, Message
from action.actor import Actor, Null

class RememberingActor(Actor):
    def __init__(self):
        self.store = []

    def handle(self, message):
        self.store.append(message)



def test_create():
    queue = MessageQueue()
    nul = Null()
    actor = RememberingActor()
    message = Message(
        target=nul, source=actor,
        data='test')
    queue.put(message)
    assert not actor.store
    queue.run_once()
    message = Message(
        target=actor, source=nul,
        data='test')
    queue.put(message)
    assert not actor.store
    queue.run_once()
    assert actor.store == [message]
