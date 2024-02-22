class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self , value):
        new_node = Node(value) #------------> O(1) # Time complexity = O(1)
        if self.head is None:   #------------> O(1) # space complexity = O(1)
            self.head = new_node #------------> O(1)
            self.tail = new_node #------------> O(1)
        else:
            self.tail.next = new_node #------------> O(1)
            self.tail = new_node

        self.length += 1 #------------> O(1)

    def insert_front(self , value):
        new_node = Node(value) #------------> O(1) # Time complexity = O(1)
        if self.head is None: #------------> O(1)  # space complexity = O(1)
            self.head = new_node #------------> O(1) 
            self.tail = new_node #------------> O(1) 
        else:
            new_node.next = self.head #------------> O(1)
            self.head = new_node
        self.length += 1 #------------> O(1)
    
    def insert_At_any_position(self , index , value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += "-->"
            temp_node = temp_node.next
        return result
        
            


Slinked_list = SingleLinkedList()
Slinked_list.append(10)
Slinked_list.append(20)
Slinked_list.insert_front(5)
Slinked_list.insert_At_any_position(1 , 100)
print(Slinked_list)
