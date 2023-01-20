# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 19:56
# @Github  : https://github.com/Leaderzhangyi
# @File    : recomend_test.py
# @Software: PyCharm
from collections import Counter
import copy

All = [str(i) + j for i in range(1, 10) for j in ("万", "条", "筒")]
All.sort(key=lambda x:(x[1],x[0]))
throw = "条" # 定的缺

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
        for num in All:
            if temp[num] >= 2 and num[1:] != throw:
                #print("num为",num)
                temp[num] -= 2
                if run(temp, count - 2, True):
                    return True
                temp[num] += 2
        return False
    else:
        for num in All:
            if num[1:] != throw and temp[num] > 0:
                #print("else中的num:", num)
                if temp[num] >= 3:  # 刻子
                    temp[num] -= 3
                    if run(temp, count - 3, True):
                        return True
                    temp[num] += 3
                if int(num[0]) + 2 <= 9 and temp[str(int(num[0]) + 1) + num[1]] > 0 and temp[str(int(num[0]) + 2) + num[1]] > 0:
                    temp[num] -= 1
                    temp[str(int(num[0]) + 1) + num[1]] -= 1
                    temp[str(int(num[0]) + 2) + num[1]] -= 1
                    if run(temp, count - 3, True):
                        return True
                    temp[num] += 1
                    temp[str(int(num[0]) + 1) + num[1]] += 1
                    temp[str(int(num[0]) + 2) + num[1]] += 1
        return False


if __name__ == '__main__':
    cards = ['4万', '5万', '6万', '7万', '1筒','2筒', '3筒', '4筒', '5筒', '6筒']
    print("手牌为：",cards,len(cards))
    res = []
    # 统计次数
    vis = Counter(cards)  # return dict
    # for num in All:
    #     if num[1:] != throw and vis[num] < 4:
    #         temp = copy.deepcopy(vis)
    #         temp[num] += 1
    #         if run(temp, len(cards)+1, False):
    #             res.append(num)
    num = '4万'
    if num[1:] != throw and vis[num] < 4:
        temp = copy.deepcopy(vis)
        temp[num] += 1
        if run(temp, len(cards) + 1, False):
            res.append(num)
    if res == []:
        print("还未听牌！！")
    else:
        print("你可以听牌：", end="")
        for item in res:
            print(item, end=" ")
