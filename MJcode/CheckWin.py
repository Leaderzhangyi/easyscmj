# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 22:24
# @Github  : https://github.com/Leaderzhangyi
# @File    : CheckWin.py
# @Software: PyCharm
import copy
from collections import Counter


class win:
    def __init__(self, throw, cards, card, isOther):
        self.AllType = [str(i) + j for i in range(1, 10) for j in ("万", "条", "筒")]
        self.AllType.sort(key=lambda x: (x[1], x[0]))
        self.throw = throw  # 定的缺
        self.cards = cards
        self.newCard = card
        self.isOther = isOther

    def check(self):
        res = []  # 听牌数组
        vis = Counter(self.cards)
        temp = copy.deepcopy(vis)
        if self.isOther:
            if self.newCard[1:] != self.throw and vis[self.newCard] < 4:
                temp[self.newCard] += 1
                if self.run(temp, len(self.cards) + 1, False):
                    return True
            return False
        else:
            for elem in self.AllType:
                if elem[1:] != self.throw and vis[self.newCard] < 4:
                    temp[elem] += 1
                    if self.run(temp, len(self.cards) + 1, False):
                        res.append(elem)
            if res == []:
                return False
            else:
                return res

    def run(self, temp, count: int, hasRun: bool):
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
            for num in self.AllType:
                if temp[num] >= 2 and num[1:] != self.throw:
                    # print("num为",num)
                    temp[num] -= 2
                    if self.run(temp, count - 2, True):
                        return True
                    temp[num] += 2
            return False
        else:
            for num in self.AllType:
                if num[1:] != self.throw and temp[num] > 0:
                    # print("else中的num:", num)
                    if temp[num] >= 3:  # 刻子
                        temp[num] -= 3
                        if self.run(temp, count - 3, True):
                            return True
                        temp[num] += 3
                    if int(num[0]) + 2 <= 9 and temp[str(int(num[0]) + 1) + num[1]] > 0 and temp[
                        str(int(num[0]) + 2) + num[1]] > 0:
                        temp[num] -= 1
                        temp[str(int(num[0]) + 1) + num[1]] -= 1
                        temp[str(int(num[0]) + 2) + num[1]] -= 1
                        if self.run(temp, count - 3, True):
                            return True
                        temp[num] += 1
                        temp[str(int(num[0]) + 1) + num[1]] += 1
                        temp[str(int(num[0]) + 2) + num[1]] += 1
            return False
