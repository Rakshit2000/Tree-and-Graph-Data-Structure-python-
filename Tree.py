import math

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root): # O(n)
    if root is None:
        return None
    inorder(root.left)
    print(root.data)
    inorder(root.right)


def preorder(root):
    if root is None:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def postorder(root): # O(n)
    if root is None:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.data)


def treeSize(root):  # O(n)
    if root == None:
        return 0
    else:
        return 1 + treeSize(root.left) + treeSize(root.right)


def get_max(root): # O(n)
    if root is None:
        return -math.inf
    return max(get_max(root.left), get_max(root.right), root.data)


def search(root, data): # O(n)
    if root is None:
        return None
    elif root.data == data:
        return True
    elif search(root.left, data) == True:
        return True
    else:
        return search(root.right, data)


def height(root):
    if root == None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
print(treeSize(root))
print()
print(get_max(root))
print()
print(search(root, 40))
print()
print(height(root))
