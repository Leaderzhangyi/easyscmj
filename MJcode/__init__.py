# -*- coding: utf-8 -*-
# @Time    : 2023-01-13 12:50
# @Github  : https://github.com/Leaderzhangyi
# @File    : __init__.py
# @Software: PyCharm

import random
import time
import copy

from collections import Counter
from Player import Player
from Robot import Robot


def CardInit():
    Cards = {(str(i) + unit): 4 for i in range(1, 10) for unit in ["万", "条", "筒"]}
    AllMa = list(Cards.keys()) * 4
    return Cards, AllMa


def GameControl():
    # 初始化牌局
    print("对局开始，正在初始化数据".center(50, '='))
    Cards, AllMa = CardInit()
    random.shuffle(AllMa)

    # 默认玩家为庄家
    print("本次你为庄家，发牌...")
    init_cards = []
    for i in range(0, 52, 13):
        init_cards.append(AllMa[i:i + 13])
    for item in init_cards:
        for j in item:
            Cards[j] -= 1

    r1, r2, r3 = (Robot(name="Robot" + str(i), cards=init_cards[i]) for i in range(1, 4))
    AllMa = AllMa[52:]  # 发了52张牌，更新牌库
    print(f"发牌完成！您的手牌如下\t牌库还有{len(AllMa)}张")
    init_cards[0].sort(key=lambda x: (x[1], x[0]))
    print(init_cards[0])
    throw = input("请你定一个缺(条 筒 万)：")
    player = Player(cards=init_cards[0], throw=throw)
    player.cards.sort(key=lambda x: (x[1], x[0]))
    print(player.cards, len(player.cards))

    gamelist = [player, r1, r2, r3]
    i = 0  # 记录初始出牌权限位置

    round = 1
    while len(AllMa) != 0:
        print(f"进行第{round}回合".center(50, '='))
        Gflag = 0
        while i < 4:
            try:
                gamelist[i].get_newCard(AllMa[0])
                del AllMa[0]
            except IndexError:
                print("本局流局，共计 %d 回合" % round)
                break
            if i != 0:  # 如果是机器人 判断每一张牌打出的牌是否满足 碰、杠
                out = gamelist[i].out
                player.judge(out)
                Gflag = player.gangflag
                win = player.Hu
                if win == 1:
                    AllMa = []
                    break
                print("Gflag为：", Gflag)
            print(f"总牌数为:{len(AllMa)}")
            # 增加机器人出牌后 判断玩家满足 碰、杠、点炮的条件？

            if Gflag == 0:
                if i == 3:
                    round += 1
                    print(f"进行第{round}回合".center(50, '='))
                    i = 0
                else:
                    i += 1


GameControl()
