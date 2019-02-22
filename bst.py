# Python program to demonstrate insert operation in binary search tree

# A utility class that represents an individual node in a BST
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with the given key
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


list = []
def search(root, node):
    if(root is not None):
        print(root.val)
    #print(root.right)
    if root is None or root.val == node:
        print("2")
        return root
    elif root.val < node:
        print("3")
        list.append("r")
        #print(node.val)
        return search(root.right, node)
    else:
        print("4")
        list.append("l")
        return search(root.left, node)



# Driver program to test the above functions
# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80

'''
r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
'''

cont = 1
command = ''

while cont == 1:
    try:
        command, value = raw_input().split()
        root = None
        if root == None:
            root = Node(value)
    except:
        pass
    command, value = [str(command), int(value)]
    if command == 'i':
        insert(root, Node(value))
    elif command == 'q':
        search(root, value)




# Print inoder traversal of the BST
#inorder(r)
