#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity # stores the maximum number of items the ring buffer can hold
        self.buffer = [None] * self.MAX_CAP # list created and length is set to capacity
        self._front = 0  # index of the least recently inserted item in the buffer
        self._rear = 0 # index one beyond the most recently inserted item in the buffer
        self._size = 0 # keeps track of the current number of items in the ring buffer

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        # TO-DO: implement this
        return self._size

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        # TO-DO: implement this
        return self._size == 0


    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this
        return self.size() == self.MAX_CAP

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        #TO-DO: implement this
        if self.is_full():
            raise RingBufferFull("Cannot enqueue into a full buffer")
        else:
            self.buffer[self._rear] = x
            self._rear = (self._rear + 1) % self.MAX_CAP
            self._size += 1


    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this
        if self.is_empty():
            raise RingBufferEmpty("Cannot dequeue from an empty buffer")
        else:
            item = self.buffer[self._front]
            self._front = (self._front + 1) % self.MAX_CAP
            self._size -= 1
            return item

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this
        if self.is_empty():
          raise RingBufferEmpty
        else:
          return self.buffer[self._front]

class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
