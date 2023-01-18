# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 11:34
# @Github  : https://github.com/Leaderzhangyi
# @File    : Player.py
# @Software: PyCharm

import random
import time
import copy
from typing import List


class Player:
    def __init__(self, cards):
        self.dice = random.randint(2, 12)
        self.cards = cards
        self.gangflag = 0
        self.pengList = []
        self.gangList = []

    def get_newCard(self, card):
        print(f"你摸到了: {card}")
        self.cards.append(card)
        #print(self.cards)
        self.cards.sort(key=lambda x: (x[1], x[0]))
        print(f"当前您的牌为：{self.cards}")
        print(f"你的碰牌为：{self.pengList}，杠牌为：{self.gangList}")

        # 操作 暗杠？ 自摸？
    def play_card(self):
        out = input("请你打出一张牌：")
        print(f"你打出了一张 {out}")
        self.cards.remove(out)

    def judge(self,other_card):
        #print("开始判断玩家是否需要: 碰 杠 胡 它人的牌为",other_c    ard) # test
        tmpCard = copy.deepcopy(self.cards)
        #tmpCard = self.cards  深浅拷贝错误！
        tmpCard.append(other_card)
        self.isPeng,self.isGang = 'n','n'
        if tmpCard.count(other_card) == 3:
            isPeng = input("是否要碰(y/n)？")
            if isPeng == 'y':
                self.Peng(other_card)

        elif tmpCard.count(other_card) == 4:
            isGang = input("是否要碰、杠、跳过(0,1,2)?")
            if isGang == 0:
                self.Peng(other_card)
            elif isGang == 1:
                self.gangflag = 1
                self.Gang(other_card)

    def Peng(self,card):
        peng_list = [card] * 3
        self.pengList.append(peng_list)
        for _ in range(2):
            self.cards.remove(card)
        self.play_card() # 碰了打出一张牌


    def Gang(self,card):
        gang_list = [card] * 4
        self.gangList.append(gang_list)
        for _ in range(3):
            self.cards.remove(card)

        # 1. 摸牌


        # 2. 打牌

