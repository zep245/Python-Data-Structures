class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

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
            self.head = new_node
        self.length += 1

    def append(self , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self , index , value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index > self.length:
            raise IndexError("Index is out of range")
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            popped_node.next = self.head.next
            self.head = popped_node.next
            popped_node = None
        self.length -= 1

    def pop_last(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            return self.tail.value
        self.length -=1 

    def pop_any(self , index):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            popped_node = self.head
            popped_node.next = self.head.next
            self.head = popped_node.next
            popped_node = None
        elif index > self.length:
            raise IndexError("Index is out of range")
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            popped_node = prev.next
            prev.next = popped_node.next
            self.tail = prev
            popped_node.next = None
        self.length -= 1

    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
        return None


    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next



linkedlist = LinkedList()
linkedlist.prepend(10)
linkedlist.append(20)
linkedlist.append(30)
linkedlist.append(40)
linkedlist.append(50)
linkedlist.append(60)
linkedlist.traverse()

print(linkedlist.head.value)
print(linkedlist.tail.value)