import collections
from threading import Lock

def BoundedBlockingQueue(Object):

    def __init__(self, capacity: int):
        self.cap = capacity
        self.eq_lock = Lock()
        self.dq_lock = Lock()
        self.que = collections.deque()
        self.dq_lock.acquire()  # Since at initialization the queue is empty, we lock the dequeue operation.
    
    def enque(self, element: int) -> None:
        self.en_lock.acquire()
        self.que.append(element)
        
        # If there is space left in the queue, we release the enque lock indicating that we can have another enque operation
        if self.size() < self.capacity:
            self.en_lock.release()
        
        # If we had locked dequeue, we can release it now because we have had atleast one enqueue implying that we can remove atleast one element from the queue.
        if self.dq_lock.locked():
            self.dq_lock.release()
    
    def deque(self) -> int:
        self.dq_lock.acquire()
        element = self.que.popleft()

        # If there is atleast one element in the queue, we release the dequeue lock indicating that we can have another dequeue operation
        if self.size() > 0:
            self.dq_lock.release()
        
        # If we had locked enqueue, we can release it now because we have had atleast one dequeue implying that we have space for atleast one more element in the queue.
        if self.en_lock.locked():
            self.eq_lock.release()
        
        return element

    def size(self) -> int:
        return len(self.que)
