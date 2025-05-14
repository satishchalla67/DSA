



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next
        print()
        
    def deleteNode(self, count):
        if self.head is None:
            return
        if count==0:
            self.head = self.head.next
        
        prev = self.head
        for _ in range(count-1):
            if prev.next is None:
                return
            prev = prev.next
        
        if prev.next is None:
            return
        
        prev.next = prev.next.next
        
    def countNodes(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count
    
    def serachNode(self, nodeData):
        temp = self.head
        
        while temp:
            if temp.data==nodeData:
                return True
            temp = temp.next
        return False
        
        
        
        
# 70 60 50 40 30 20 10

llist = LinkedList()
llist.insertAtEnd(70)
llist.insertAtEnd(60)
llist.insertAtEnd(50)
llist.insertAtEnd(40)
llist.insertAtEnd(30)
llist.insertAtEnd(20)
llist.insertAtEnd(10)
llist.printLinkedList()
# llist.deleteNode(3)
# llist.printLinkedList()
# print(llist.countNodes())
print(llist.serachNode(0))