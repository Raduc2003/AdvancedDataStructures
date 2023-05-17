class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.parent = None
        self.val = val


class BST:
    def __init__(self):
        self.tree = set([])
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            currentNode = self.root
            newNode = Node(key)
            while newNode.parent == None:
                if newNode.val < currentNode.val:
                    if currentNode.left != None:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                        newNode.parent = currentNode
                if newNode.val >= currentNode.val:
                    if currentNode.right != None:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode
                        newNode.parent = currentNode

    def firstBelow(self, key):
        currentNode = self.root
        bestMatch = None
        while currentNode != None:
            if currentNode.val <= key:
                bestMatch = currentNode
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        if bestMatch is None:
            return None
        else:
            return bestMatch.val

    def firstAfter(self, key):
        currentNode = self.root
        bestMatch = None
        while currentNode != None:
            if currentNode.val >= key:
                bestMatch = currentNode
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        if bestMatch is None:
            return None
        else:
            return bestMatch.val

    def findKey(self, key):
        currentNode = self.root
        while currentNode != None:
            if currentNode.val == key:
                return 1, currentNode
            elif currentNode.val > key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return 0

    def remove(self, key):
        found, currentNode = self.findKey(key)
        if found:
            if currentNode.left is None and currentNode.right is None:
                if currentNode.parent is None:
                    self.root = None
                elif currentNode.parent.left == currentNode:
                    currentNode.parent.left = None
                else:
                    currentNode.parent.right = None
            elif currentNode.left is None:
                if currentNode.parent is None:
                    self.root = currentNode.right
                    currentNode.right.parent = None
                elif currentNode.parent.left == currentNode:
                    currentNode.parent.left = currentNode.right
                    currentNode.right.parent = currentNode.parent
                else:
                    currentNode.parent.right = currentNode.right
                    currentNode.right.parent = currentNode.parent
            elif currentNode.right is None:
                if currentNode.parent is None:
                    self.root = currentNode.left
                    currentNode.left.parent = None
                elif currentNode.parent.left == currentNode:
                    currentNode.parent.left = currentNode.left
                    currentNode.left.parent = currentNode.parent
                else:
                    currentNode.parent.right = currentNode.left
                    currentNode.left.parent = currentNode.parent
            else:
                replaceNode = currentNode.left
                while replaceNode.right is not None:
                    replaceNode = replaceNode.right
                currentNode.val = replaceNode.val
                if replaceNode.parent.left == replaceNode:
                    replaceNode.parent.left = replaceNode.left
                    if replaceNode.left is not None:
                        replaceNode.left.parent = replaceNode.parent
                else:
                    replaceNode.parent.right = replaceNode.left
                    if replaceNode.left is not None:
                        replaceNode.left.parent = replaceNode.parent

def printBST(root):
    if root != None:
        printBST(root.left)
        print(root.val)
        printBST(root.right)


def printBSTBetween(root, start, end):
    if root is None:
        return

    if start < root.val:
        printBSTBetween(root.left, start, end)

    if start <= root.val <= end:
        print(root.val, end=' ')

    if root.val < end:
        printBSTBetween(root.right, start, end)

# tree = BST()
# tree.insert(7)
# tree.insert(5)
# tree.insert(9)
# tree.insert(3)
# tree.insert(6)
# tree.insert(8)
# tree.insert(11)
# tree.insert(10)
# tree.insert(12)
# tree.insert(2)
# tree.insert(4)
# tree.insert(4.5)
# # print(tree.firstAfter(5.1))
# printBST(tree.root)
# tree.remove(n)
# print("after removing")
# printBST(tree.root)
# print('asdads')
# printBSTBetween(tree.root,7,10)
