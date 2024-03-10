class Stack:
    def __init__(self):
        self.list = []


    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        return self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.list = None
            
    def traverse(self):
        value = [value for value in self.list]
        print(value)
        

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.traverse()
stack.pop()
stack.traverse()
print(stack.peek())