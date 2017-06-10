# code = utf-8

"""三人斗地主手牌规则：
一副牌 54 张（4 种花色各 13 张，大小王），一人 17 张，留 3 张做底牌。
 
要求：
将一副牌随机打乱（洗牌）后分配给 3 位玩家（发牌），输出每个人的手牌和剩余底牌。
 
可使用 list 和 random 完成。"""

import random
result = []
list_num = range(1, 14)
list_color = ['桃', '杏', '梅', '方']
list_king = ['大王', '小王']

for i in list_num:
    for j in list_color:
        item = j + str(i)
        result.append(item)
#print(result)
for k in list_king:
    result.append(k)
#print(result)

person_01 = random.sample(result, 17)
print('玩家1的手牌：' + str(person_01))
person_02 = random.sample(list(set(result) - set(person_01)), 17)
print('玩家2的手牌：' + str(person_02))
person_03 = random.sample(list(set(result) - set(person_01) - set(person_02)), 17)
print('玩家3的手牌：' + str(person_03))
rest = list(set(result) - set(person_01) - set(person_02) - set(person_03))
print('剩余底牌：' + str(rest))