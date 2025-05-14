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
        return self.container.pop()
    def size(self):
        return len(self.container)

def generate_binary_numbers(n):
    s = Queue()
    s.enqueue("1")
    res = []
    
    for i in range(n):
        current = s.dequeue()
        res.append(current)
        s.enqueue(current+"0")
        s.enqueue(current+"1")
    return res
    


result = generate_binary_numbers(10)
for res in result:
    print(res)
    