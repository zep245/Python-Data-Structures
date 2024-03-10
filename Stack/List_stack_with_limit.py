class Stack:
    def __init__(self , maxLimit):
        self.maxLimit = maxLimit
        self.list = []


    def traverse(self):
        value = [value for value in self.list]
        print(value)

    def isFull(self):
        if len(self.list) == self.maxLimit:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self , value):
        if self.isFull():
            raise ValueError("The stack is full")
        else:
            return self.list.append(value)
        
    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        else:
            return self.list[len(self.list) -1 ]
        
    def delete(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        else:
            self.list = None
       


stack = Stack(4)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.peek())