"""
script info:
name: deque 双端队列
"""


class Deque(object):
    """
    deque implementation
    双端队列实现
    """

    def __int__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addHead(self, item):
        self.items.append(item)

    def addEnd(self, item):
        self.items.insert(0, item)

    def removeHead(self):
        self.items.pop()

    def removeEnd(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    print(__doc__)
