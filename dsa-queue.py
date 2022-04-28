"""
script info:
name: queue 队列
"""

class Queue(object):
    """
    queue implementation
    队列实现
    """

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items[-1]
        # return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    print(__doc__)

    string_queue=Queue()

    string_queue.enqueue('a')
    print(string_queue.items)
    