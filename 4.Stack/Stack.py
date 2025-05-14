# Stack is LIFO kind of data stucture
# LAST IN FIRST OUT


from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def is_Empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
        

s = Stack()
s.push(10)
s.push(20)

print(s.size())
print(s.is_Empty())
print(s.pop())
print(s.pop())
print(s.size())
print(s.is_Empty())