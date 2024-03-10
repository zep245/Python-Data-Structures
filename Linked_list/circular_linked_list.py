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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length += 1

    def append(self , value):
        new_node= Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1


    def insert(self ,index , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.prev = self.tail
            self.tail.next = self.head
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev  = self.tail
            self.tail.next = self.head
        else:
            head_node = self.head
            for _ in range(index-1):
                head_node = head_node.next
            new_node.next = head_node.next
            new_node.pre = head_node
            head_node.next.prev = new_node
            head_node.next = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            popped_node.next = self.head.next
            self.head = self.head.next
            popped_node = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1

    def pop_last(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail = popped_node.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1

    def pop_any(self , index ):
        current_node = self.head
        if index >= self.length:
            raise IndexError("Index is out of range")
        if index== 0:
            self.head = self.head.next
            self.head.prev = self.tail
        if index == self.length -1:
            return self.pop_last()
        else:
            for _ in range(index):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            current_node = None
        self.length -= 1
        


    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value , end=" ")
            current_node = current_node.next
            if current_node == self.head:
                break
    def delete(self):
        self.head = None
        self.tail = None
        self.length = 0
        print("All nodes deleted")

linked = LinkedList()

linked.prepend(10)
linked.append(20)
linked.append(30)
linked.append(40)
linked.insert(0 , 100)

# linked.pop_last()
# linked.pop_last()
linked.pop_any(1)




