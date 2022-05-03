"""
script info:
name logic gate 逻辑门
ref: http://39.100.145.216/p/view/ac449bec-1d4b-4358-9c59-78babb1c812d/
"""


class LogicGate(object):
    """
    logic gate superclass
    """

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()

        return self.output


class BinaryGate(LogicGate):
    """
    binary gate
    二元逻辑门
    """

    # version 1
    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA=None
        self.pinB=None

    # # version 2
    # def __int__(self, n):
    #     super(BinaryGate, self).__init__(n)
    #
    # # version 3
    # def __index__(self, n):
    #     super().__init__(n)

    def getPinA(self):
        if self.pinA is None:
            return int()


if __name__ == '__main__':
    print(__doc__)



