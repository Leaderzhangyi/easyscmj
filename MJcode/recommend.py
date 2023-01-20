# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 15:24
# @Github  : https://github.com/Leaderzhangyi
# @File    : recommend.py
# @Software: PyCharm

# 思路
# 1. 统计所有数字出现的次数
# 2. 循环补充一个数字，凑成14个数字
# 3. 循环选取次数2以及以上的数字为雀头
# 4. 排除雀头，递归判断剩下12个数字是否可以组成刻子或者顺子，如果能够符合规则，记录次数
# 5. 返回数据
from collections import Counter
from typing import List
import copy

def run(temp, count: int, hasRun: bool):
    """
    :param temp: 临时字典变量
    :param count: 牌组数量
    :param hasRun: 是否判断对子
    :return: bool变量
    """
   # print("每次递归的temp:",temp)
    if count == 0:
        return True  # 可以胡牌
    if not hasRun:
        for num in range(1, 10):
            if temp[num] >= 2:
                temp[num] -= 2
                if run(temp, count - 2, True):
                    return True
                temp[num] += 2
        return False
    else:
        for num in range(1,10):
            if temp[num] > 0:
                if temp[num] >= 3: # 刻子
                    temp[num] -= 3
                    if run(temp,count - 3,True):
                        return True
                    temp[num] += 3
                if num + 2 <= 9 and temp[num+1]>0 and temp[num+2] > 0:
                    temp[num] -= 1
                    temp[num + 1] -= 1
                    temp[num + 2] -= 1
                    if run(temp,count - 3,True):
                        return True
                    temp[num] += 1
                    temp[num + 1] += 1
                    temp[num + 2] += 1
        return False

if __name__ == '__main__':
    cards = [1, 1, 1, 1, 2, 2, 3, 3, 5, 6, 7, 8, 9]
    # vis = []
    res = []
    # 统计次数
    vis = Counter(cards)  # return dict
    for num in range(1, 10):
        if vis[num] < 4:
            temp = copy.deepcopy(vis)
            temp[num] += 1
            if run(temp, 14, False):
                res.append(num)

    if res == []:
        print("还未听牌！！")
    else:
        print("手牌为：",cards)
        print("你可以听牌：", end="")
        for item in res:
            print(item, end=" ")
