#-*- codeing = utf-8 -*-
#@Time : 2021/3/19 16:11
#@Author : 骆龙飞
#@File : v2.py
#@Software : PyCharm


# 排序
def sortList(list):
    for i in range(len(list)):
        for j in range(i,len(list)):
            if(list[i] <= list[j]):
                continue;
            else:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp


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

# 查看列表中是否有该列表
def haveList(valuelist,list):
    temp = 0
    for item in valuelist:
        temp += haveValue(item,list)
    if temp == len(valuelist):
        return 1
    else:
        return 0

# 去重(处理列表)
def handleList(userinput):
    # 排序
    userinput.sort()
    # 去重
    userinput = list(set(userinput))
    return userinput

# 给出结果
def result(list):
    # 分析是哪一种动物
    if haveList([10,12,16,17],list):
        if list == [10,12,16,17]:
            print("完全符合金钱豹的特征，该动物就是金钱豹")
        print("黄褐色，身上有暗斑点,哺乳动物，食肉动物->金钱豹")
        print("该动物为金钱豹的可能：",4/len(list))
        return 0
    if list == [10,12,16,18]:
        print("黄褐色，有黑色条纹，哺乳动物，食肉动物->老虎")
        print("该动物为老虎")
        return 0
    if list == [14,17,19,20]:
        print("有暗斑点，有长腿，长脖子，有蹄类动物->长颈鹿")
        print("该动物为长颈鹿")
        return 0
    if list == [14,18]:
        print("有黑色条纹，有蹄类动物->斑马")
        print("该动物为斑马")
        return 0
    if list == [11,19,20,21,22]:
        print("不会飞，长脖子，长腿，鸟类->鸵鸟")
        print("该动物为鸵鸟")
        return 0
    if list == [11,21,22,23]:
        print("不会飞，会游泳，有黑白二色，鸟类->企鹅")
        print("该动物为企鹅")
        return 0
    if list == [11,24]:
        print("善飞，鸟类->信天翁")
        print("该动物为信天翁")
        return 0
    else:
        print("不知道是哪一种动物")
        return -1


# 分析推理过程
def analyze(list):

    if haveValue(1,list):
        print("有毛->哺乳动物")
        del list[list.index(1)]
        if haveValue(10,list):
            pass;
        else:
            list.append(10)

    if haveValue(2,list):
        print("有奶->哺乳动物")
        del list[list.index(2)]
        if haveValue(10, list):
            pass;
        else:
            list.append(10)

    if haveValue(3,list):
        print("有羽毛->是鸟")
        del list[list.index(3)]
        if haveValue(11,list):
            pass;
        else:
            list.append(11)

    if haveValue(6,list):
        print("吃肉->食肉动物")
        del list[list.index(6)]
        if haveValue(12,list):
            pass;
        else:
            list.append(12)

    if haveValue(4,list) and haveValue(5,list):
        print("会飞，会下蛋->是鸟")
        del list[list.index(4)]
        del list[list.index(5)]
        if haveValue(11,list):
            pass;
        else:
            list.append(11)

    if haveValue(7,list) and haveValue(8,list) and haveValue(9,list):
        print("犬齿，有爪，眼盯前方->食肉动物")
        del list[list.index(7)]
        del list[list.index(8)]
        del list[list.index(9)]
        if haveValue(12,list):
            pass;
        else:
            list.append(12)

    if haveValue(10,list) and haveValue(13,list):
        print("哺乳动物，有蹄->有蹄类动物")
        del list[list.index(10)]
        del list[list.index(13)]
        if haveValue(14,list):
            pass;
        else:
            list.append(14)

    if haveValue(10, list) and haveValue(15, list):
        print("哺乳动物，反刍动物->有蹄类动物")
        del list[list.index(10)]
        del list[list.index(15)]
        if haveValue(14,list):
            pass;
        else:
            list.append(14)


if __name__ == '__main__':
    print('''输入对应条件前面的数字:
                                        *******************************************************
                                        *1:有毛  2:有奶  3:有羽毛  4:会飞  5:会下蛋          *
                                        *6:吃肉  7:有犬齿  8:有爪  9:眼盯前方  10:哺乳动物        *
                                        *11:是鸟  12:食肉动物  13:有蹄  14:有蹄类动物  15:反刍动物 *
                                        *16:黄褐色  17:身上有暗斑点  18:黑色条纹  19:长脖子  20:有长腿   *
                                        *21：不会飞  22:有黑白二色  23:会游泳  24：善飞              *
                                        *******************************************************
                                        *******************当输入数字0时!程序结束***************
        ''')
    userinput = []
    # temp = 24
    while True:
        try:
            inp = int(input("请输入条件前的数字："))
        except Exception as e:
            continue;
        if inp>0 and inp<25:
            # 假如有相违背的条件，阻止输入(可以选择这个功能)
            # if(haveValue(4,userinput) and inp == 21) or (haveValue(21,userinput) and inp == 4):
            #     continue;
            userinput.append(inp)
        elif inp == 0:
            break;
        else:
            print("当前输入不在条件内：",inp)

    print(userinput)

    if(len(userinput) != 0):

        userinput = handleList(userinput)
        print(userinput)

        sortList(userinput)
        print(userinput)

        analyze(userinput)

        sortList(userinput)
        print(userinput)

        result(userinput)



