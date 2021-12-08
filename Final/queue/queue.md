#Python Queue Tutorial

- [back](../welcome.md)

**Introduction of Queue:**
    Queue can be considered as a list which has a rule: FIFO(First in first out).
    The picture below is to illustate how Queue works.
    
    In this tutorial, Enqueue and Dequeue will be introduced which are the basic concepts of Queue.

**Example of queue:**
    When it comes to queue, we must use FIFO rule. The best example can be used in a hospital. The earlier patients arrive, the earlier doctor appointments they can do.

The queue functions is below:

```python
class Queue:
    def __init__(self):
        self.waiting_list = []

    def isEmpty(self):
        if self.waiting_list ==[]:
            return print('Now is empty')
        else :
            return print('Now is not empty')
    def enqueue(self, person): 
        self.waiting_list.insert(0,person)

    def dequeue(self):     
        return self.waiting_list.pop()

    def size(self):
        return len(self.person)
```


**Enqueue:**
    The first patient will be put as the first one of the list. Who comes later will be put after the previous one. We will use enqueue function to insert them into the list. 
    The Big O of enqueue is O(1).

```python
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"Enterence {queue.waiting_list} Doctor")
```

Output:
    
    Enterence [3, 2, 1] Doctor
The earlier is put in the waiting list, the closer to the doctor.


**Dequeue:**
    The patient will be dequeue from the list is the closet one to the doctor. We will use dequeue function to take off them from the list.
    The Big O of dequeue is O(1).
    
```python
    print(f"Enterence {queue.waiting_list} Doctor")
    result = queue.dequeue()
    print(f"Enterence {queue.waiting_list} Doctor {result}")
    print()

    print(f"Enterence {queue.waiting_list} Doctor")
    result = queue.dequeue()
    print(f"Enterence {queue.waiting_list} Doctor {result}")
    print()

    print(f"Enterence {queue.waiting_list} Doctor")
    result = queue.dequeue()
    print(f"Enterence {queue.waiting_list} Doctor {result}")
    print()


    print(f"Enterence {queue.waiting_list} Doctor")
```

**Question or Challenge:**
- [Challenge](queue-Q.py)

**Answer:**
- [Answer](queue-A.py)

# - [back](../welcome.md)