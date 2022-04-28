class Stack(object):
    """
    栈 implementation
    """

    def __int__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
        # return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    print(Stack.__doc__)