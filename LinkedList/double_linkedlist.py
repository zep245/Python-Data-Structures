class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def insert(self , index , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index > self.length:
            raise IndexError("Index out of range")
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index -1 ):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
            self.tail = None
        else:
            popped_node = self.head
            self.head.next = popped_node.next
            self.head = popped_node.next
            popped_node = None
        self.length -= 1

    def pop_last(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail.prev = popped_node.prev
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node = None
        self.length -= 1

    def pop_any(self , index):
        popped_node = self.head
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop_last()    
        else:
            for _ in range(index):
                popped_node = popped_node.next
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
        self.length -= 1

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0

linkedlist = LinkedList()
linkedlist.prepend(10)
linkedlist.append(20)
linkedlist.append(30)
linkedlist.append(40)
linkedlist.append(50)
linkedlist.append(60)
linkedlist.append(70)
linkedlist.insert(7 , 100)
linkedlist.traverse()