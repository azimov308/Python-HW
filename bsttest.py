class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertNode(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertNode(root.left, node)


list = []
def search(root, key):
    if(root is not None):
        print(root.val)
    #print(root.right)
    if root is None or root.val == key:
        print("2")
        return root
    elif root.val < key:
        print("3")
        list.append("r")
        #print(node.val)
        return search(root.right, key)
    else:
        print("4")
        list.append("l")
        return search(root.left, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


cont = 1
command = ''

while (True):
        command = input()
        try:
            command, value= command.split()
        except:
            if(command == "quit"):
                break

        if command == "i":
            try:
                insertNode(r,Node(value))
                print("inserted Node")
            except:
                r = Node(value)
                print("Made root")
        elif command == "q":
            try:
                searchNode(r, value)
            except:
                print("Tree not started")
        else:
            print("invalid")

inorder(r)
