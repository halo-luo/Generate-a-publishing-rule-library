#-*- codeing = utf-8 -*-
#@Time : 2021/3/20 21:28
#@Author : 骆龙飞
#@File : 1.py
#@Software : PyCharm


list = [1,1,22,3,5,6]

# 查看列表是否有该元素
def haveValue(value,list):
    for i in range(0, len(list)):
        if (list[i] == value):
            return 1
        else:
            if (i != len(list) - 1):
                continue
            else:
                return 0

def haveList(valuelist,list):
    temp = 0
    for item in valuelist:
        temp += haveValue(item,list)
    if temp == len(valuelist):
        return 1
    else:
        return 0

print(haveList([1,3,],list))


