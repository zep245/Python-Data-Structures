class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()


    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
        
    def push(self , value):
        new_node = Node(value)
        new_node.next = self.linkedlist.head
        self.linkedlist.head = new_node

    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            current_node = self.linkedlist.head
            current_node.next = self.linkedlist.head.next
            self.linkedlist.head = current_node.next
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.linkedlist.head.value

    def delete(self):
        self.linkedlist.head = None

    
    def traverse(self):
        current = self.linkedlist.head
        while current is not None:
            print(current.value)
            current = current.next

        
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.traverse()
stack.pop()
print(stack.peek())