


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
            temp=temp.next
        print()
        
    def detectCycle(self):
        slow = self.head
        fast = self.head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow==fast:
                return True
        return False
        
        
        
        
        
        
# 70,60,50,40,30,20,10
llist = LinkedList()
llist.insertAtEnd(70)
llist.insertAtEnd(60)
llist.insertAtEnd(50)
llist.insertAtEnd(40)
llist.insertAtEnd(30)
llist.insertAtEnd(20)
llist.insertAtEnd(10)
print("Linked list: ")
llist.printLinkedList()
llist.head.next.next.next.next.next.next = llist.head
if llist.detectCycle():
    print("Cycle is detected inside the loop")
else:
    print("Cycle is not detected")