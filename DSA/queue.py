
# _____________________________________________________________________ Queue First In, First Out (FIFO) principle _______________________________________________________________________________________________#

# Queue: A queue is a collection of elements with two principal operations: enqueue, which adds an element to the
# rear of the queue, and dequeue which removes an element from the front of the queue. Queues follow the First In,
# First Out (FIFO) principle, meaning that the first element added to the queue is the first one to be removed.

#      NOTE    #

# The Queue class implements the basic functionalities of a queue using a Python list.
# enqueue(item) adds an item to the rear of the queue.
# dequeue() removes and returns the item from the front of the queue.
# peek() returns the item at the front of the queue without removing it.
# is_empty() checks if the queue is empty.
# size() returns the size of the queue.
# This implementation follows the First In, First Out (FIFO) principle, where elements are added to the rear and removed from the front of the queue.



class Queue:
    def __init__(self):
        self.items=[]

    def is_Empty(self):
        return self.items==0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_Empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_Empty():
            return self.items[0]

    def size(self):
        return len(self.items)


# Creating a queue

queue=Queue()
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)

print('Queue: ',queue.items)
print("Queue:", queue.items)
print("Front of Queue:", queue.peek())
print("Dequeued item:", queue.dequeue())
print("Queue after dequeue:", queue.items)
