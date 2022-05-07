"""
script info:
name: dynamic programming
"""


def dpMakeChange(coinValueList, change, minCoins):
    """
    动态规划实现找零兑换
    Args:
        coinValueList: 硬币找零体系
        change: 待找零余额
        minCoins:

    Returns:

    """
    # 从最小开始求最优解
    # 从1分开始到change逐个计算最少硬币数
    for cents in range(1, change + 1):
        # 初始化最大值
        coin_count = cents
        # 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coin_count:
                coin_count = minCoins[cents - j] + 1
        minCoins[cents] = coin_count

    return minCoins[change]


def dpMakeChange2(coinValueList, change, minCoins, coinsUsed):
    """
    动态规划实现找零兑换
    Args:
        coinValueList: 硬币找零体系
        change: 待找零余额
        minCoins:

    Returns:

    """
    # 从最小开始求最优解
    # 从1分开始到change逐个计算最少硬币数
    for cents in range(1, change + 1):
        # 初始化最大值
        coin_count = cents
        # 初始化新加硬币
        new_coin = 1
        # 减去每个硬币，向后查最少硬币数，同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coin_count:
                coin_count = minCoins[cents - j] + 1
                new_coin = j
        minCoins[cents] = coin_count
        coinsUsed[cents] = new_coin
    return minCoins[change]


if __name__ == '__main__':
    print(__doc__)

    print(dpMakeChange([1, 5, 20, 21, 25], 63, [0] * 64))
