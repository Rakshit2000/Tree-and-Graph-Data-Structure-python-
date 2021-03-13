class BST:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def insert(root, key): # Recursive O(h)
    if root is None:
        return BST(key)
    elif root.key == key:
        return root
    elif root.key > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


# Recursive Search O(height)
def search_BST(root, key):
    if root is None:
        return False
    elif root.key == key:
        return True
    elif root.key > key:
        return search_BST(root.left, key)
    else:
        return search_BST(root.right, key)


# Iterative Search O(height)
def searchBST(root, key):
    while root is not None:
        if root.key == key:
            return True
        elif root.key > key:
            root = root.left
        else:
            root = root.right
    return False


def del_node(root, key): # O(h)
    if root.key is None:
        return
    elif root.key > key:
        root.left = del_node(root.left, key)
    elif root.key < key:
        root.right = del_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = get_suc(root.right, key)
            root.key = succ
            root.right = del_node(root.right, succ)
    return root


def get_suc(curr, key):
    while curr.left is not None:
        curr = curr.left
    return curr.key


def get_floor(root, key):  # O(h)
    res = None
    while root is not None:
        if root.key == key:
            return root
        elif root.key > key:
            root =  root.left
        else:
            res = root
            root =  root.right
    return res


def get_ceil(root, key): # O(h)
    res = None
    while root is not None:
        if root.key == key:
            return root
        elif root.key < key:
            root = root.left
        else:
            res = root
            root = root.right
    return res



root = None
root = insert(root, 10)
insert(root, 20)
insert(root, 5)
insert(root, 2)
insert(root, 25)
insert(root, 30)
print(searchBST(root, 80))
del_node(root, 5)
print(searchBST(root, 5))









