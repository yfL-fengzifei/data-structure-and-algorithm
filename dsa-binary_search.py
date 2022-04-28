"""
script info:
[name] binary search 二分查找
"""


class BinarySearch():
    """
    binary search implemetation
    二分查找的实现
    """

    def search_iterative(self, l: list, item: int):
        """
        iterative search 迭代搜索
        Args:
            l: 待查找的list [list]
            item: 待查找的数值 int

        Returns:
            对应的list索引
        """

        head = 0
        end = len(l) - 1

        while head <= end:
            mid = (head + end) // 2

            guess = l[mid]

            if guess == item:
                return mid
            elif guess > item:
                end = mid - 1
            else:
                head = mid + 1

        return None

    def search_recursive(self, l, head, end, item):
        """
        recursive search 递归搜索
        Args:
            l: 待查找的列表
            head: 列表首索引
            end: 列表尾索引
            item: 待查找的元素

        Returns:
            找到的list索引
        """

        if head <= end:

            mid = (head + end) // 2

            guess = l[mid]

            if guess == item:
                return mid
            elif guess > item:
                return self.search_recursive(l, head, mid - 1, item)
            else:
                return self.search_recursive(l, mid + 1, end, item)

        else:
            return None


if __name__ == '__main__':
    print(__doc__)

    bs = BinarySearch()

    l = [1, 3, 5, 7, 9]
    item2search = 3

    # iterative search
    print(bs.search_iterative(l, item2search))

    # recursive search
    print(bs.search_recursive(l, 0, len(l) - 1, item2search))
