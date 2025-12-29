






class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
       

def preorder(root):
    stack=[root]
    
    while stack:
        curr=stack.pop()
        print(curr.data, end=" ")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
            
def inorder(root):
    stack=[]
    curr=root
    
    while True:
        if curr:
            stack.append(curr)
            curr=curr.left
        elif stack:
            curr=stack.pop()
            print(curr.data, end=" ")
            curr=curr.right
        else:
            break

def postorder(root):
    stack1=[root]
    stack2=[]
    
    while stack1:
        curr=stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        curr=stack2.pop()
        print(curr.data,end=" ")








# ABDECF
# DBEAFC
# DEBFCA



root = Node('A')
root.left=Node('B')
root.right=Node('C')
root.left.left = Node('D')
root.left.right=Node('E')
root.right.left=Node('F')
preorder(root)
print()
inorder(root)
print()
postorder(root)
print()