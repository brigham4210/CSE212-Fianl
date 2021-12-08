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
        
 
print("Test")
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
# start from here

#========================
print(queue.list)