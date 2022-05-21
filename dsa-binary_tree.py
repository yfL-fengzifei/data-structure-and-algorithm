"""
script info:
name: binary tree 二叉树 的 列表实现
"""


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    print(__doc__)

    r = BinaryTree(3)
    print(r)
    insertLeft(r, 4)
    print(r)
    insertLeft(r, 5)
    print(r)
    insertRight(r, 6)
    print(r)
    insertRight(r, 7)
    print(r)
    # print(r)

    l = getLeftChild(r)
    print(l)
