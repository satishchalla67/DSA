



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def printLinkedList(self):
        if self.head is None:
            print("No linked is to print.")
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp = temp.next
        print()
        
    def insertAtNode(self, prevNode, data):
        new_node = Node(data)
        new_node.next = prevNode.next
        prevNode.next = new_node
    
    def getNode(self, count):
        temp = self.head
        while count>1:
            temp = temp.next
            count-=1
        return temp
    
    def reverseLinkedList(self):
        curr = self.head
        prev = None
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
         
llist = LinkedList()
llist.insertAtBegining(10)
llist.insertAtBegining(20)
llist.insertAtBegining(30)
llist.insertAtEnd(40)
llist.insertAtEnd(50)
llist.insertAtEnd(60)
llist.insertAtEnd(70)
llist.printLinkedList()
prevnode = llist.getNode(3)
llist.insertAtNode(prevnode, 80)
llist.insertAtNode(llist.head, 90)
llist.printLinkedList()
llist.reverseLinkedList()
llist.printLinkedList()

# 30 20 10 40 50 60 70
# 30 90 20 10 80 40 50 60 70