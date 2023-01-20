# -*- coding: utf-8 -*-
# @Time    : 2023-01-18 11:34
# @Github  : https://github.com/Leaderzhangyi
# @File    : Robot.py
# @Software: PyCharm
import time
import copy
import random
from typing import List

class Robot:
    def __init__(self, name: str, cards: List[str]):
        self.name = name
        self.dice = random.randint(a=2, b=12)
        self.cards = cards

    def get_newCard(self, card):
        self.cards.append(card)
        self.cards.sort(key=lambda x: (x[1], x[0]))
        #print(f"1.机器人{self.name}的手牌为：{self.cards}")
        self.out = self.play_card(card)
        #print(f"2.机器人{self.name}的手牌为：{self.cards}")


    def play_card(self, card):
        print(self.name + "出的牌为：", card)
        self.cards.remove(card)
        return card