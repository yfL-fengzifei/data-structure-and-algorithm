"""
script info:
name: binary tree 二叉树 的 链表实现
"""


class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rigChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preOrder(self):
        print(self.key)

        if self.leftChild:
            self.leftChild.preOrder()

        if self.rightChild:
            self.rightChild.preOrder()

    def postOrder(self):

        if self.leftChild:
            self.leftChild.preOrder()

        if self.rightChild:
            self.rightChild.preOrder()

        print(self.key)

    def inOrder(self):
        if self.leftChild:
            self.leftChild.preOrder()

        print(self.key)

        if self.rightChild:
            self.rightChild.preOrder()


def preOrder(tree):
    """
    先序遍历
    Args:
        tree: 待遍历的树结构

    Returns:
        None
    """
    if tree:  # is None
        print(tree.getRootVal())
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())


def postOrder(tree):
    """
    后序遍历
    Args:
        tree: 待遍历的树结构

    Returns:
        None
    """
    if tree is not None:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print(tree.getRootVal())


def inOrder(tree):
    """
    中序遍历
    Args:
        tree: 待遍历的树结构

    Returns:
        None
    """
    if tree is not None:
        inOrder(tree.getLeftChild())
        print(tree.getRootVal())
        inOrder(tree.getRightChild())


if __name__ == '__main__':
    print(__doc__)
    r = BinaryTree('a')
    print(r.key, r.getRootVal(), r.getLeftChild(), r.getRightChild())

    r.insertLeft('b')
    r.insertRight('c')

    r.getRightChild().setRootVal('hello')

    r.getLeftChild().insertRight('d')
