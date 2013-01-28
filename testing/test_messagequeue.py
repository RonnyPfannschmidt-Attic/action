from functools import partial
from action.messages import MessageQueue, Message
from action.actor import Actor, Null, QueueActor

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


def test_handle_result():
    
    class ResultActor(Actor):
        def handle(self, message):
            return [message._replace(data=message.data+1)]
    
    queue = MessageQueue()

    r = ResultActor()
    queue.put(Message(source=None,target=r,data=1))
    queue.run_once()
    assert len(queue.messages) == 1
    assert queue.messages[0].data ==2


def test_queue():
    queue = MessageQueue()
    actor = RememberingActor()
    q = QueueActor()
    mm = partial(Message, source=actor, target=q)
    queue.put(mm(data=('get', None)))
    queue.put(mm(data=('put', 'some')))
    queue.put(mm(data=('get', None)))
    queue.put(mm(data=('get', None)))
    queue.run_all()


    data = [x.data for x in actor.store]
    assert data == [
        ('empty', None),
        ('item', 'some'),
        ('empty', None),
    ]



