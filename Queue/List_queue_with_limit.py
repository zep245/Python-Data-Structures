class Queue:
    def __init__(self , maxLimit):
        self.list = []
        self.maxLimit = maxLimit

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxLimit:
            return True
        else:
            return False
        
    def enqueue(self , value):
        if self.isFull():
            raise Exception("Queue is full")
        else:
            return self.list.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.list.pop(0)
        
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.list[0]
        
    def delete(self):
        self.list = None


    def traverse(self):
        value = [value for value in self.list]
        print(value)

queue = Queue(3)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.peek())