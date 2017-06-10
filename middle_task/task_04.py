# code = utf-8

"""在微信发群红包，设定了总金额和总人数之后，每个人能抢到多少红包是随机的。
要求：使用函数模拟一个随机分配红包的方法


参考文章：用 Python 实现一个简单的微信红包算法（http://mp.weixin.qq.com/s?__biz=MjM5MDEyMDk4Mw==&mid=402183699&idx=1&sn=f5c12abeec90d32eca177dce2b1ca467）
 
主要涉及内容：随机数
"""

import random
person_amount = []
def red_pkg(money, cnt):
    total = money * 100
    money = money * 100
    for i in range(1,cnt + 1):
        if i < cnt:
            amount = random.randint(1,int(money - (cnt-i)))
            #print(amount)
            person_amount.append(amount)
            money -= amount
            #print(person_amount)
        else:
            sum = 0
            for j in person_amount:
                sum += j
            person_amount.append(total - sum)
            #print(sum)
            #print(person_amount)

    return [j /100 for j in person_amount]

money = int(input('请输入红包金额：'))
cnt = int(input('请输入红包数：'))
print(red_pkg(money, cnt))
