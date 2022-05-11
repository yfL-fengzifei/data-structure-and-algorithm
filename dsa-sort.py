"""
script info:
name: sort algorithm 各种排序实现
"""


def bubbleSort(l: list) -> list:
    """
    bubble sort 冒泡排序
    Args:
        l: 待排序列表 list

    Returns:
        排序的结果列表 list
    """

    for passnum in range(len(l) - 1, 0, -1):
        for i in range(passnum):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l


def selectionSort(l: list) -> list:
    """
    selected sort
    选择排序
    Args:
        l: 待排序列表 list

    Returns:
        排序的结果列表 list
    """

    # version1
    for fillsort in range(len(l) - 1, 0, -1):
        position0fMax = 0
        for location in range(1, fillsort + 1):
            if l[location] > l[position0fMax]:
                position0fMax = location

        l[fillsort], l[position0fMax] = l[position0fMax], l[fillsort]

    return l


def insertSort(l: list) -> list:
    """
    insert sort
    插入排序
    Args:
        l: 待排序列表 list

    Returns:
        排序的结果列表 list

    """
    for index in range(1, len(l)):
        currentvalue = l[index]
        position = index

        while position > 0 and l[position - 1] > currentvalue:
            l[position] = l[position - 1]
            position = position - 1

        l[position] = currentvalue

    return l


def mergeSort(l: list) -> list:
    """
    merge sort implemented by recursion
    递归实现归并排序
    Args:
        l: 待排序列表 list

    Returns:
        排序的结果列表 list

    """
    if len(l) > 1:
        mid = len(l) // 2
        left_half = l[:mid]
        right_half = l[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l[k] = left_half[i]
                i += 1
            else:
                l[k] = right_half[j]
                j += 1
            k += 1

        # 归并左右 半部剩余部项
        while i < len(left_half):
            l[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            l[k] = right_half[j]
            j += 1
            k += 1

    return l


def mergeSort2(l: list) -> list:
    """
    merge sort implemented by recursion
    递归实现归并排序
    Args:
        l: 待排序列表 list

    Returns:
        排序的结果列表 list

    """
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left_half = mergeSort2(l[:mid])
    right_half = mergeSort2(l[mid:])

    merge = []
    while left_half and right_half:
        if left_half[0] <= right_half[0]:
            merge.append(left_half.pop(0))
        else:
            merge.append(right_half.pop(0))

    merge.extend(right_half if right_half else left_half)
    return merge


def quickSort(l: list, first: int = 0, last: int = -1) -> list:
    """
    quick sort implemented by recusion
    递归实现快速排序
    Args:
        l:
        first:
        last:

    Returns:

    """
    if first < last:
        # split 分裂
        splitpoint = partition(l, first, last)

        quickSort(l, first, splitpoint - 1)
        quickSort(l, splitpoint + 1, last)

    return l

def partition(l: list, first: int = 0, last: int = -1):
    """

    Args:
        l:
        first:
        last:

    Returns:

    """
    # 选择中值
    pivotvalue = l[first]

    # 左右标
    leftmark = first + 1
    rightmark = last

    # 左右标移动结束
    done = False

    while not done:
        # 左标右移
        while (leftmark <= rightmark and
               l[leftmark] <= pivotvalue):
            leftmark += 1

        # 右标左移
        while (leftmark <= rightmark and
               l[rightmark] >= pivotvalue):
            rightmark -= 1

        if rightmark < leftmark:  # 左右标交错，则停止移动
            done = True
        else:  # 交换左右标所指元素
            l[leftmark], l[rightmark] = l[rightmark], l[leftmark]

    # 交换中值
    l[first], l[rightmark] = l[rightmark], l[first]

    return rightmark

if __name__ == '__main__':
    print(__doc__)

    l = [1, 0, 54, 3, 2, 77, 99]

    """bubble sort"""
    # 无返回值
    # bubbleSort(l)
    # print(l)

    # 有返回值
    # print(bubbleSort(l.copy()))

    print("""selected sort""")
    print(selectionSort(l.copy()))

    print("""insert sort""")
    print(insertSort(l.copy()))

    print("""merge sort: version1""")
    print(mergeSort(l.copy()))

    print("""merge sort: version2""")
    print(mergeSort2(l.copy()))

    print("""quick sort""")
    print(quickSort(l.copy(),0,len(l)-1))