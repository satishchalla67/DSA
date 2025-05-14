# insetAtBegining
# insetAtEnd
# printLinkedList
# insertAferNode
# getNode
# reverseLinkedList
# detectCycle
# deleteNode
# countNode
# searchNode
# sortLinkedList


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
    
    def getNode(self, count):
        temp = self.head
        while count>0 and temp.next:
            temp = temp.next
            count-=1
        return temp
    
    def insertAfterNode(self, prevNode, data):
        new_node = Node(data)
        if prevNode is None:
            return "Invalid Node"
        new_node.next = prevNode.next
        prevNode.next = new_node
        
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
        
    def detectCycle(self):
        temp = self.head
        slow =  temp
        fast = temp.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
    
    def deleteNode(self, node_data):
        if self.head.data == node_data:
            self.head = self.head.next
        temp = self.head
        while temp.next:
            if temp.next.data==node_data:
                temp.next = temp.next.next
                return
            temp=temp.next
            
    def countNode(self):
        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count
    
    def searchNode(self, node_data):
        temp = self.head
        count = -1
        while temp:
            count+=1
            if temp.data == node_data:
                return count
            temp = temp.next
        return -1
    
    def convertCircular(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = self.head
    
    
def mergeLinkedList(list1, list2):
    dummy = Node(0)
    tail = dummy
    
    temp1 = list1.head
    temp2 = list2.head
    
    while temp1 and temp2:
        if temp1.data < temp2.data:
            tail.next = temp1
            temp1 = temp1.next
        else:
            tail.next = temp2
            temp2 = temp2.next
        tail = tail.next
        
    tail.next = temp1 if temp1 else temp2
            
    merged = LinkedList()
    merged.head = dummy.next
    return merged

# 40 30 20 50 10 90 100
llist = LinkedList()
llist.insertAtBegining(10)
llist.insertAtBegining(50)
llist.insertAtBegining(20)
llist.insertAtBegining(30)
llist.insertAtBegining(40)
llist.insertAtEnd(90)
llist.insertAtEnd(100)
llist.printLinkedList()
print(llist.detectCycle())
llist.convertCircular()
print(llist.detectCycle())








# prevNode = llist.getNode(13)
# llist.insertAfterNode(prevNode, 120)
# llist.printLinkedList()
# llist.reverseLinkedList()
# llist.printLinkedList()

# Detect cycle
# print(llist.detectCycle())
# prevNode = llist.getNode(6)
# prevNode.next = llist.head
# print(llist.detectCycle())

# Delete Node
# llist.deleteNode(40)
# llist.printLinkedList()

# print(llist.countNode())

# print(llist.searchNode(100))



# llist1 = LinkedList()
# llist1.insertAtBegining(10)
# llist1.insertAtBegining(50)
# llist1.insertAtBegining(20)
# llist1.insertAtBegining(30)
# llist1.insertAtBegining(40)
# llist1.insertAtEnd(90)
# llist1.insertAtEnd(100)

# llist2 = LinkedList()
# llist2.insertAtBegining(11)
# llist2.insertAtBegining(55)
# llist2.insertAtBegining(44)
# llist2.insertAtBegining(22)
# llist2.insertAtBegining(33)
# llist1.printLinkedList()
# llist2.printLinkedList()



# list3 = mergeLinkedList(llist1, llist2)
# list3.printLinkedList()