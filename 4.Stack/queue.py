# add 0 and 1 at the end to each number
# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000
# 1001
# 1010

# till n=10

from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
        
    def enqueue(self, val):
        return self.container.appendleft(val)
    
    def dequeue(self):
        return self.container.pop() if self.container else None
    
    def size(self):
        return len(self.container)
    
    
    
def generate_binary_numbers(n):
    if n<=0:
        return []
    
    q = Queue()
    q.enqueue("1")
    result = []
    
    
    for i in range(n):
        current = q.dequeue()
        result.append(current)
        q.enqueue(current+"0")
        q.enqueue(current+"1")
        
    return result

result = generate_binary_numbers(10)

for res in result:
    print(res)