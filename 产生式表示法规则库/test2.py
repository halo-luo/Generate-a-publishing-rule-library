#-*- codeing = utf-8 -*-
#@Time : 2021/3/19 11:57
#@Author : 骆龙飞
#@File : v1.py
#@Software : PyCharm


# 动物识别系统
# 虎、金钱豹、斑马、长颈鹿、企鹅、鸵鸟、信天翁 等7种动物

# 快排
def quickSort(list,begin,end):
    while begin > end:
        return list
    # 如果区间不只有一个元素（begin < end）
    if(begin < end):
        temp = list[begin]
        i = begin
        j = end
        while(i < j):
            while(i < j and list[j] > temp):
                j = j - 1
            list[i] = list [j]
            while(i < j and list[i] <= temp):
                i = i + 1
            list[j] = list[i]
        list[i] = temp
        quickSort(list,begin,i-1)
        quickSort(list,i+1,end)

# 判断列表中是否有该元素
def judge_repeat(value, list=[]):
    for i in range(0, len(list)):
        if (list[i] == value):
            return 1
        else:
            if (i != len(list) - 1):
                continue
            else:
                return 0


def analyze(list):

    for item in range(len(list)):
        for i in list:
            # 判断金钱豹和虎
            if (i == 23):
                for i in list:
                    if (i == 12):
                        for i in list:
                            if (i == 21):
                                for i in list:
                                    if (i == 13):
                                        print("黄褐色，有斑点,哺乳类，食肉类->金钱豹\n")
                                        print("所识别的动物为金钱豹")
                                        return 0
                                    elif (i == 14):
                                        print("黄褐色，有黑色条纹，哺乳类，食肉类->虎\n")
                                        print("所识别的动物为虎")
                                        return 0

            # 斑马
            elif (i == 14):
                for i in list:
                    if (i == 24):
                        print("有黑色条纹，蹄类->斑马\n")
                        print("所识别的动物为斑马")
                        return 0

            # 长颈鹿
            elif (i == 24):
                for i in list:
                    if (i == 13):
                        for i in list:
                            if (i == 15):
                                for i in list:
                                    if (i == 16):
                                        print("有斑点，有黑色条纹，长脖，蹄类->长颈鹿\n")
                                        print("所识别的动物为长颈鹿")
                                        return 0

            # 信天翁
            elif (i == 20):
                for i in list:
                    if (i == 22):
                        print("善飞，鸟类->信天翁\n")
                        print("所识别的动物为信天翁")
                        return 0

            # 鸵鸟
            elif (i == 22):
                for i in list:
                    if (i == 4):
                        for i in list:
                            if (i == 15):
                                for i in list:
                                    if (i == 16):
                                        print("不会飞，长脖，长腿，鸟类->鸵鸟\n")
                                        print("所识别的动物为鸵鸟")
                                        return 0

            # 企鹅
            elif (i == 4):
                for i in list:
                    if (i == 22):
                        for i in list:
                            if (i == 18):
                                for i in list:
                                    if (i == 19):
                                        print("不会飞，会游泳，黑白二色，鸟类->企鹅\n")
                                        print("所识别的动物企鹅")
                                        return 0

            elif(list.index(i) != len(list)-1):
                continue;
    print("\n根据所给条件无法判断为何种动物")


# 推理过程
def process(list_real):

    for i in list_real:
        if (i == 1):
            if (judge_repeat(21, list_real) == 0):
                list_real.append(21)
                print("有毛发->哺乳类")
        elif (i == 2):
            if (judge_repeat(21, list_real) == 0):
                list_real.append(21)
                print("产奶->哺乳类")
        elif (i == 3):
            if (judge_repeat(22, list_real) == 0):
                list_real.append(22)
                print("有羽毛->鸟类")
        else:
            if (list_real.index(i) != len(list_real) - 1):
                continue
            else:
                break
    for i in list_real:
        if (i == 4):
            for i in list_real:
                if (i == 5):
                    if (judge_repeat(22, list_real) == 0):
                        list_real.append(22)
                        print("不会飞，会下蛋->鸟类")
        elif (i == 6):
            for i in list_real:
                if (i == 21):
                    if (judge_repeat(21, list_real) == 0):
                        list_real.append(21)
                        print("食肉->哺乳类")
        elif (i == 7):
            for i in list_real:
                if (i == 8):
                    for i in list_real:
                        if (i == 9):
                            if (judge_repeat(23, list_real) == 0):
                                list_real.append('23')
                                print("有犬齿,有爪,眼盯前方->食肉类")
        elif (i == 10):
            for i in list_real:
                if (i == 21):
                    if (judge_repeat(24, list_real) == 0):
                        list_real.append(24)
                        print("有蹄，哺乳类->蹄类")
        elif (i == 11):
            for i in list_real:
                if (i == 21):
                    if (judge_repeat(24, list_real) == 0):
                        list_real.append(24)
                        print("反刍，哺乳类->蹄类")
        else:
            if (i != len(list_real) - 1):
                continue
            else:
                break
    # return list_real



if __name__ == '__main__':

    print('''输入对应条件前面的数字:
                                    *******************************************************
                                    *1:有毛发  2:产奶  3:有羽毛  4:不会飞  5:会下蛋          *
                                    *6:吃肉  7:有犬齿  8:有爪  9:眼盯前方  10:有蹄         *
                                    *11:反刍  12:黄褐色  13:有斑点  14:有黑色条纹  15:长脖 *
                                    *16:长腿  17:会飞  18:会游泳  19:黑白二色  20:善飞   *
                                    *21：哺乳类  22:鸟类  23:食肉类  24：蹄类              *
                                    *******************************************************
                                    *******************当输入数字0时!程序结束***************
    ''')

    userinput = []
    while True:
        try:
            inp = int(input("请输入条件前的数字："))
        except Exception as e:
            continue;
        if(inp > 0 & inp < 25):
            for item in range(len(userinput)):
                if(userinput[item] == inp):
                    break;
            userinput.append(inp)
            continue;
        elif(inp == 0):
            print(userinput)
            # 循环结束时，数组已经准备好了
            break;
        else:
            print("当前输入不在条件内：")
    quickSort(userinput,0,len(userinput)-1)
    print(userinput)

    process(userinput)
    # userinput = process(userinput)
    # print(userinput)
    analyze(userinput)
