class Queue:
    '''class that represents a queue'''
    
    def __init__(self, queue = []):
        '''initializes the queue to an empty queue'''
        self.queue = queue

    def enqueue(self, item):
        '''(Queue, Oject)-> None
        adds an item to the end of the queue'''
        (self.queue).insert(len(self.queue), item)

    def dequeue(self):
        '''(Queue)->Object
        removes and returns the element at the front of the queue'''
        return (self.queue).pop(0)

    def isEmpty(self):
        '''(Queue)->Booleans
        returns True if the queue is empty'''
        if len(self.queue) < 1:
            return True
        return False

    def __eq__(self, other):
        '''(Queue, Queue)->Boolean
        returns True if self is equal to other'''
        return self.queue == other.queue

    def __repr__(self):
        '''(Queue)->String
        formal representation of queue'''
        return 'Queue(' + str(self.queue) + ')'

    def __len__(self):
        '''(Queue)->Integer
        returns the length of the queue'''
        return len(self.queue)
