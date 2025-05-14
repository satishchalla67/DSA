



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
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
        

def mergeLinkedlist(llist1, llist2):
    # Outplace sorting
    merged = Linkedlist()
    temp1 = llist1.head
    temp2 = llist2.head
    while temp1 and temp2:
        if temp1.data<temp2.data:
            merged.insertAtEnd(temp1.data)
            temp1 = temp1.next
        else:
            merged.insertAtEnd(temp2.data)
            temp2 = temp2.next
    
    while temp1:
        merged.insertAtEnd(temp1.data)
        temp1 = temp1.next
    while temp2:
        merged.insertAtEnd(temp2.data)
        temp2 = temp2.next
    
    return merged

def mergeLinkedlist2(llist1, llist2):
    # Inplace sorting
    dummy = Node(0)
    tail = dummy
    temp1 = llist1.head
    temp2 = llist2.head
    while temp1 and temp2:
        if temp1.data < temp2.data:
            tail.next = temp1
            temp1 = temp1.next
        else:
            tail.next = temp2
            temp2 = temp2.next
        tail = tail.next
    
    tail.next = temp1 if temp1 else temp2
    
    merged = Linkedlist()
    merged.head = dummy.next
    return merged


def sortLinkedlist(head1, head2):
    
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    temp = None
    
    if head1.data < head2.data:
        temp = head1
        temp.next = sortLinkedlist(head1.next, head2)
    else:
        temp = head2
        temp.next = sortLinkedlist(head1, head2.next)
    
    return temp
        
        
        
           
llist1 = Linkedlist()
llist1.insertAtEnd(10)
llist1.insertAtEnd(30)
llist1.insertAtEnd(50)
llist1.insertAtEnd(70)

llist2 = Linkedlist()
llist2.insertAtEnd(20)
llist2.insertAtEnd(40)
llist2.insertAtEnd(60)
llist2.insertAtEnd(80)
llist2.insertAtEnd(100)
llist2.insertAtEnd(120)

llist1.printLinkedList()
llist2.printLinkedList()


merged1 = mergeLinkedlist(llist1, llist2)
merged1.printLinkedList()

merged2 = mergeLinkedlist2(llist1, llist2)
merged2.printLinkedList()


merged3 = sortLinkedlist(llist1.head, llist2.head)
merged3.printLinkedList()

# 10 30 50 70
# 20 40 60 80














