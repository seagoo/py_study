# code = utf-8

"""BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字

BMI < 18.5 体重偏轻
18.5 <= BMI < 24 体重正常
BMI >= 24 体重偏重

设计一个BMI计算器吧，看看自己体重是否正常。
输入：身高、体重值
输出：BMI 指数、是否正常
"""
def bmi(height, weight):
    bmi_value = weight / (height * height)
    if bmi_value < 18.5:
        result = '体重偏轻'
    elif 18.5 <= bmi_value < 24:
        result = '体重正常'
    elif bmi_value >= 24:
        result = '体重偏重'
    return [str(bmi_value), result]

height = float(input('请输入您的身高（米）：'))
print(height)
weight = float(input('请输入您的体重（公斤）：'))
print(weight)
print('BMI 指数：' + bmi(height, weight)[0])
print('您的' + bmi(height, weight)[1])
