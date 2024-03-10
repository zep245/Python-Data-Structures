class Queue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self , value):
        return self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[0]

    def delete(self):
        self.list = None

    def traverse(self):
        value = [value for value in self.list]
        print(value)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.peek())
queue.traverse()