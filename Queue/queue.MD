# Queue

A queue is a container of objects that are inserted and removed according to the FIRST-IN-FIRST-OUT principl, aka elements enter at the rear and removed at the front. It runs in O(1) time complexity and takes up O(n) space.

![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/440px-Data_Queue.svg.png "Queue Operations")

## Main Queue Operations

1. Init():  Initializes the queue to empty.
2. enqueue(o): insert object o at the rear of the queue
3. dequeue(): remove and return from the queue the object at the front; error occurs if queue is empty


## Auxilliary Operations

1. first(): returns the last inserted element without removing it.
2. size(): returns the number of elements stored
3. isEmpty(): indicates whether no elements are stored

