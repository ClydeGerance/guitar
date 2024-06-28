#!/usr/bin/env python3
from ringbuffer import *
import random
import math

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 24000 Hz
        '''
        # TO-DO: implement this
        self.capacity = math.ceil(44100 / frequency) 
        self.buffer = RingBuffer(self.capacity) 
      
        for i in range(self.capacity): 
          self.buffer.enqueue(0) 
                                
        self.ticks = 0

    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000) 

        stg.capacity = len(init)  
        stg.buffer = RingBuffer(stg.capacity)

        for x in init:
            stg.buffer.enqueue(x)

        return stg

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # TO-DO: implement this
        for i in range(self.capacity):
            self.buffer.dequeue()
            self.buffer.enqueue(random.uniform(-1/2,1/2))

    def tick(self): # pinapatunog na gitara
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # TO-DO: implement this
        first = self.buffer.dequeue()
        second = self.buffer.peek()
        new = 0.996 * ((first+second)/2)   
                    
        self.buffer.enqueue(new)
        self.ticks += 1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        # TO-DO: implement this
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        # TO-DO: implement this
        return self.ticks
        
