class Queue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if self.list ==[]:
            return print('Now is empty')
        else :
            return print('Now is not empty')
    def enqueue(self, item): 
        self.list.insert(0,item)

    def dequeue(self):     
        return self.list.pop()

    def size(self):
        return len(self.item)
        

print("Test")
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.dequeue() # take off 1
queue.dequeue() # take off 2

queue.enqueue(0) # add 0
queue.enqueue(0)
print(queue.list)