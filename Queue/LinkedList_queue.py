class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.list = LinkedList()


    def isEmpty(self):
        if self.list.head is None:
            return True
        else:
            return False
        
    def enqueue(self , value):
        new_node = Node(value)
        if self.list.head is None:
            self.list.head = new_node
            self.list.tail = new_node
        else:
            self.list.tail.next = new_node
            self.list.tail = new_node

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            current = self.list.head
            current.next = self.list.head.next
            self.list.head = current.next
            current = None

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            return self.list.head.value

    def traverse(self):
        current = self.list.head
        while current is not None:
            print(current.value)
            current = current.next

    def delete(self):
        self.list.head = None
        self.list.tail = None

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.traverse()
queue.dequeue()
print("-------------")
queue.traverse()