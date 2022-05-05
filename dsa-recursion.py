"""
script info:
name: resursion 递归
"""

import sys


def recursionSum(l: list) -> int:
    """
    list sum implemented by recursion
    递归实现进制转换
    Args:
        l: list 待求和的元素

    Returns:
        sum: int
    """
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + recursionSum(l[1:])


def binHexOct(n: int, base: int) -> str:
    """
    number system transformation implemented by recursion
    递归实现进制转换
    Args:
        n: number 待转换数字
        base: 进制转换基

    Returns:
        进制转换结果 str
    """
    convert_string = '0123456789'
    if base > 10:
        convert_string = '0123456789ABCDEF'

    if n < base:
        return convert_string[n]  # str
    else:
        return binHexOct(n // base, base) + convert_string[n % base]  # 因为返回的str 所以可以用+进行拼接


def fractalTree(branch_len: int):
    """
    fractal tree
    分型树
    Args:
        branch_len:

    Returns:

    """
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        fractalTree(branch_len - 15)
        t.left(40)
        fractalTree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


def hanoi():
    """
    tower of hanoi implemented by recursion
    递归实现汉诺塔
    Returns:

    """

    def moveTower(height, fromPole, withPole, toPole):
        if height >= 1:
            moveTower(height - 1, fromPole, toPole, withPole)
            moveDisk(height, fromPole, toPole)
            moveTower(height - 1, withPole, fromPole, toPole)

    def moveDisk(disk, fromPole, toPole):
        print(f'moving disk[{disk}] from {fromPole} to {toPole}')

    moveTower(3,'#1','#2','#3')


if __name__ == '__main__':
    print(__doc__)

    print(sys.getrecursionlimit())
    # print(sys.setrecursionlimit()) # 设置递归栈最大深度

    # 递归求解 数列求和
    print(recursionSum([1, 3, 5, 7, 9]))

    # 进制转换
    print(binHexOct(123456, 16))

    # import turtle
    #
    # t = turtle.Turtle()
    # t.left(90)
    # t.penup()
    # t.backward(100)
    # t.pendown()
    # t.pencolor('green')
    # t.pensize(3)
    # fractalTree(75)
    # t.hideturtle()
    # turtle.done()

    hanoi()