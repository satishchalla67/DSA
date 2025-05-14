




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insetAtBegining(self, data):
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
        temp = self.head
        while temp:
            print(str(temp.data), end=" ")
            temp=temp.next
        print()
        
    def insertAfterNode(self, prevNode, data):
        new_node = Node(data)
        new_node.next = prevNode.next
        prevNode.next = new_node
        
    def getNode(self, num):
        temp = self.head
        while num>1:
            temp = temp.next
            num-=1
        return temp
    
    
    def reverseLinkedList(self):
        curr=self.head
        prev=None
        next=None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
            
            
            
llist = LinkedList()
llist.insetAtBegining(30)
llist.insetAtBegining(20)
llist.insetAtBegining(10)
llist.insertAtEnd(40)
llist.insertAtEnd(60)
prevNode = llist.getNode(4)
llist.insertAfterNode(prevNode, 50)
llist.printLinkedList()
