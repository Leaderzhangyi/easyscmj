# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 11:34
# @Github  : https://github.com/Leaderzhangyi
# @File    : Player.py
# @Software: PyCharm

import random
from CheckWin import win
import copy
from typing import List

All = [str(i) + j for i in range(1, 10) for j in ("万", "条", "筒")]
All.sort(key=lambda x: (x[1], x[0]))


class Player:
    def __init__(self, cards, throw):
        self.dice = random.randint(2, 12)
        self.cards = cards
        self.throw = throw  # 定缺
        self.gangflag = 0
        self.Hu = 0
        self.pengList = []
        self.gangList = []

    def get_newCard(self, card):
        print(f"你摸到了: {card}")
        self.cards.append(card)
        # print(self.cards)
        self.cards.sort(key=lambda x: (x[1], x[0]))
        print(f"当前您的牌为：{self.cards},张数为：{len(self.cards)}")
        print(f"你的碰牌为：{self.pengList}，杠牌为：{self.gangList}")
        self.play_card()

        # 操作 暗杠？ 自摸？

    def play_card(self):
        out = input("请你打出一张牌：")
        print(f"你打出了一张 {out}")
        self.cards.remove(out)

    def judge(self, other_card): # 用于判定机器人打出的牌
        result = ""
        tmpCard = copy.deepcopy(self.cards)
        # tmpCard = self.cards  深浅拷贝错误！
        tmpCard.append(other_card)
        self.isPao = self.check_Pao(tmpCard,other_card,isOther=True) #判定

        if tmpCard.count(other_card) == 3 or tmpCard.count(other_card) == 4 or self.isPao:

            if tmpCard.count(other_card) == 3 and tmpCard.count(other_card) == 4 and self.isPao:
                result = "请选择操作[碰:0 杠:1 胡:2 跳过:3]   输入(0,1,2,3)："
            elif tmpCard.count(other_card) == 3 and self.isPao:
                result = "请选择操作[碰:0 杠:1(不可用) 胡:2 跳过:3]   输入(0,1,2,3)："
            elif tmpCard.count(other_card) == 3:
                result = "请选择操作[碰:0 杠:1(不可用) 胡:2(不可用) 跳过:3]   输入(0,1,2,3)："
            elif self.isPao:
                result = "请选择操作[碰:0(不可用) 杠:1(不可用) 胡:2 跳过:3]   输入(0,1,2,3)："
                print(self.isPao)
            option = input(result)
            while True:
                if option not in ['0','1','2','3']:
                    print("输入有误！请重新输入!")
                    option = input(result)
                elif option == '0':
                    self.Peng(other_card)
                    break
                elif option == '1':
                    # 杠的逻辑
                    self.gangflag = 1
                    self.Gang(card=other_card)
                    break
                elif option == '2':
                    # 加上胡的类型
                    print("你胡了！！游戏结束")
                    self.Hu = 1
                    break
                elif option == '3':
                    break


    def Peng(self, card: str):
        peng_list = [card] * 3
        self.pengList.append(peng_list)
        for _ in range(2):
            self.cards.remove(card)
        self.play_card()  # 碰了打出一张牌

    def Gang(self, card: str):
        gang_list = [card] * 4
        self.gangList.append(gang_list)
        for _ in range(3):
            self.cards.remove(card)
        self.gangflag = 1 #杠标记为 1

        # 还需实现：
        # 1. 摸牌
        # 2. 打牌
        # 3. 杠上开花？


    def check_Pao(self, tmpCard, card: str, isOther: bool) -> bool:
        return win(self.throw, tmpCard, card, isOther).check()
