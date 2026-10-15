class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def _height(node):
    return node.height if node else 0


def _update_height(node):
    node.height = 1 + max(_height(node.left), _height(node.right))


def _balance(node):
    return _height(node.left) - _height(node.right)


def _rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    _update_height(y)
    _update_height(x)
    return x


def _rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    _update_height(x)
    _update_height(y)
    return y


def _insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = _insert(node.left, key)
    elif key > node.key:
        node.right = _insert(node.right, key)
    else:
        return node  # ignore duplicates

    _update_height(node)
    b = _balance(node)

    if b > 1 and key < node.left.key:
        return _rotate_right(node)
    if b < -1 and key > node.right.key:
        return _rotate_left(node)
    if b > 1 and key > node.left.key:
        node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if b < -1 and key < node.right.key:
        node.right = _rotate_right(node.right)
        return _rotate_left(node)

    return node


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = _insert(self.root, key)

    def contains(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self):
        result = []

        def walk(node):
            if node:
                walk(node.left)
                result.append(node.key)
                walk(node.right)

        walk(self.root)
        return result

    def height(self):
        return _height(self.root)


def bubble_sort(arr):
    arr = list(arr)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return list(arr)

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)