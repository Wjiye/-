"""
*****原神_模拟抽卡*****

*By Oyasumi233
*2020/10/12
*程序版本：V1.3.0

*更新人物时，可直接在前几行的列表中修改,无需修改主程序
*仅为计算机二级考试与github练手使用
"""

from random import *
allDraw=10
lsNoPutAll=[]

rangeStart=10
fiveC=["氪晴","77","琴","莫娜","温迪","卢老爷"]
fiveW=["天空之翼","西风原典","天空之卷","和璞鸢","狼的末路","天空之刃","风鹰剑","天空之傲","天空之脊"]
fourC=["砂糖","重云","诺艾尔","班尼特","谢菲尔","凝光","行秋","北斗","香菱","安柏","雷泽","凯亚","芭芭拉","丽莎"]
fourW=["弓藏","祭礼弓","绝弦","西风猎弓","昭心","祭礼残章","流浪乐章","西风秘典","西风长枪","匣里灭辰","雨裁","祭礼大剑","钟剑","西风大剑","匣里龙吟","祭礼剑","笛剑","西风剑"]
threeW=["弹弓","神射手之誓","鸦羽弓","翡玉法球","讨龙英杰谭","魔道绪论","黑鹰枪","以理服人","沐浴龙血的剑","铁鹰剑","飞天御剑","黎明神剑","冷刃"]


def main():
    infoPrint()
    drawIngMain()
    a=input("")
    print("\n\n")
    global allDraw
    if (a=="1"):
        allDraw += 10
        main()

def infoPrint():
    print("Start!,按1回车继续")
    
def drawIngMain():
    #抽卡主函数
    global lsNoPutAll
    lsNoPut2=OnesGet()
    lsNoPutAll=lsNoPutAll+lsNoPut2
    lsChangedNoPut = lsChange(lsNoPut2,lsNoPutAll)
    drewStart(lsChangedNoPut)
    
def drewStart(lsChangedNoPut):
    #输出视觉效果
    for i in range(rangeStart):
        a=max(lsChangedNoPut)
        if (a==5):
            print("\033[0;33;40m{:}\033[0m".format(chr(10022))*5 ,end="")
            b=randint(0,(len(fiveC)+len(fiveW)-1))
            if (0<=b<(len(fiveC))):
                print("\033[0;33;40m{:}\033[0m".format(fiveC[b]+"  角色"))
            else:
                print("\033[0;33;40m{:}\033[0m".format(fiveW[b-6]+"  武器"))

        elif (a==4):
            print("\033[0;35;40m{:}\033[0m".format(chr(10022)*4) ,end="")
            c=randint(0,len(fourW)+len(fourC)-1)
            if (0<=c<(len(fourC)-1)):
                print("\033[0;35;40m{:}\033[0m".format(fourC[c]+"  角色"))
            else:
                print("\033[0;35;40m{:}\033[0m".format(fourW[c-14]+"  武器"))
        elif (a==3):
            print(chr(10022)*3,end="")
            d=randint(0,(len(threeW)-1))
            print(threeW[d])
        lsChangedNoPut.remove(a)

def lsChange(lsNoPut2,lsNoPutAll):
    #保底机制，没有BUG了别乱改
    global allDraw
    if (4 not in lsNoPut2):
        lsNoPut2.remove(3)
        lsNoPut2.append(4)
        print("\033[0;34;40m{:}\033[0m".format("保底的4星"))
    if (5 in lsNoPutAll):
        allDraw=0
        lsNoPutAll.clear()
    if(allDraw==90 and 5 not in lsNoPutAll):
        lsNoPut2.remove(3)
        lsNoPut2.append(5)
        allDraw=0
        lsNoPutAll.clear()
        print("\033[0;34;40m{:}\033[0m".format("保底的5星......"))
    fileRem(lsNoPut2)
    taunt(lsNoPutAll,lsNoPut2)
    return lsNoPut2

def getFileData():
    #文件读取相关，还没写
    pass
    
def fileRem(lsNoPut2):
    f=open("temp.txt",'a+')
    ls=str(lsNoPut2)
    f.write(ls)

def OnesGet():
    #抽卡的核心代码
    lsNoPut=[]
    for i in range(rangeStart):
        tvRanInt=randint(0,1000)
        if (tvRanInt<943):
            lsNoPut.append(3)
        elif(943<=tvRanInt<994):
            lsNoPut.append(4)
        elif(994<=tvRanInt<=1000):
            lsNoPut.append(5)
    return lsNoPut

def taunt(lsChangedNoPut,lsNoPut2):
    global lsNoPutAll
    if (lsNoPutAll==80):
        print("\033[0;34;40m{:}\033[0m".format("保底5星"))
    if (lsNoPutAll==10 and 5 in lsNoPut2):
        print("\033[0;34;40m{:}\033[0m".format("NB"))
main()
