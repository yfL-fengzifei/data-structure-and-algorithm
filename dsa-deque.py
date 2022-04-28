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


def backToWord(s: str):
    """
    回文词实现
    Args:
        s: string 待检测的字符串

    Returns:

    """
    string_deque = Deque()

    for x in s:
        string_deque.addEnd(x)

    # version1
    equal = True
    while string_deque.size() > 1 and equal:
        head = string_deque.removeHead()
        end = string_deque.removeEnd()

        if head != end:
            equal = False
    return equal


if __name__ == '__main__':
    print(__doc__)

    # string_deque=Deque()
    # print(string_deque.__doc__)
    # print(dir(string_deque))

    # backToWord('radar')

    #check word weather back equal
    # print(backToWord('radar'))
    # print(backToWord('dfhjfdhgfjdhgf'))
