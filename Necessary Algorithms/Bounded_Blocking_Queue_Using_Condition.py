from threading import Condition

def BoundedBlockingQueue(Object):

    def __init__(self, capacity: int):
        self.cap = capacity
        self.condition = Condition()
        self.que = collections.deque()
    
    def enque(self, element: int) -> None:
        self.condition.acquire()
        try:
            while self.size() == self.cap:
                self.condition.wait()   # wait while the queue is full
            self.que.append(element)
            self.condition.notifyAll()
        finally:
            self.condition.release()
    
    def deque(self) -> int:
        self.condition.acquire()
        try:
            while self.size() == 0:
                self.condition.wait()   # wait while the queue is empty
            element = self.que.popleft()
            self.condition.notifyAll()
            return element
        finally:
            self.condition.release()

    def size(self) -> int:
        return len(self.que)
