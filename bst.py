class Node:
    def __init__(self, i):
        self.left = None
        self.right = None
        self.val = i


def insertNode(root, node):
    root = node
    if root is None:
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


def searchNode(root, i):
    if root is None or root.val == i:
        return root
        if root.val < i:
            return searchNode(root.right, i)
        else:
            return searchNode(root.left, i)


cont = 1
while (cont == 1):
    try:
        command, value = raw_input().split()
    except:
        if command is None and value is None:
            print ("invalid input")
            break
        elif command == 'i':
            node = value
            insertNode(node, value)
        elif command == 'q':
            searchNode(node, value)
'''
i 1
i 2
i 3

q 1 # prints "found: root"
q 2 # prints "found: r"
q 3 # prints "found: r r"
q 4 # prints "not found"


[1,2,3]
so... 1 is the root
when you query for 2, in order, it would go [root, r]
                            so that's why it prints "found: r"
when you query for 3, in order, it would go [root, r, r]
                            so that's why it prints "found: r, r"
when you query for 4, in order, it would go []<--no var in tree matches 4
                            so that's why it prints "not found"

is that the correct logic?

"found: r r 1 r"
^^What does this mean exactly???
'''
