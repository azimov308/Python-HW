class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
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



def search(root, key):
    if root is None:
        print("not found")
    if root.val == key and len(list) > 0:
        print("found: " + ' '.join(map(str, list)))
        return root
    elif root.val < key:
        list.append("r")
        return search(root.right, key)
    elif root.val > key:
        list.append("l")
        return search(root.left, key)
    elif len(list) == 0 and root.val == key:
        print("found root")


cont = 1
command = ''
value = None
while (True):
        command = input()
        try:
            command, value= command.split()
            if firstroot is None:
                firstroot = value
        except:
            if(command == "quit"):
                break
        try:
            value = int(value)
            if(value is None):
                #print("invalid")
                pass
            elif command == "i":
                try:
                    insertNode(r,Node(value))
                    #print("inserted Node")
                except:
                    r = Node(value)
                    #print("Made root")
            elif command == "q":
                try:
                    list = []
                    search(r, value)
                except:
                    pass
            else:
                #print("invalid")
                pass
        except:
                #print("value needs to be a number")
                pass
