import color
import test_co as co
import test_lis_test_printer as key
import keyboard
import time
import random


size_max_y = 30
size_max_X = 104

size_X, size_Y = size_max_X,size_max_y

paltau = co.creat_mat(size_X,size_Y)

x = round(size_max_X/2)
y = round(size_max_y/2)

def pomme():
    paltau = co.creat_mat(size_max_X,size_max_y)
    for i in range(1, 72):
        xpom = random.randint(0, size_max_X -1)
        ypom = random.randint(1, size_max_y -1)
        try:
            paltau[ypom][xpom] = "☁️ "  #chr(0x1F388) #chr(0x1F34E)
        except:
            print("x", len(paltau[0]), "y", len(paltau) ,":" , "x",[xpom],"y",[ypom])
            print(paltau[ypom][xpom])
            time.sleep(50)
    return paltau


paltau = pomme()

YV = 0
XV = 0

VVX = 0
VVY = 0

while not keyboard.is_pressed("esc"):
    color.color.clear()

    if abs(XV) < 0.001:
        XV = 0
        x = round(x)

    if key.keyboard_pres()["right"] and y > size_max_y - 1:
        XV += 0.8
    if key.keyboard_pres()["left"] and y > size_max_y - 1:
        XV += -0.8


    x += XV + VVX
    XV /= 1.173

    if key.keyboard_pres()["down"]:
        y += 1
    if key.keyboard_pres()["up"]:
        if y > size_max_y - 1:
            YV = -4

    if key.keyboard_pres()["space"]:
        x = round(size_max_X / 2)
        y = 0
        YV = 1
        XV = 0

    if key.keyboard_pres()["t"]:
        x = 3
        y = size_max_y - 3
        XV = 5
        YV = -4.5
        print("PAUSSE\n" * 1)
        co.afV2(paltau, round(x), round(y))
        time.sleep(0.7)
        color.color.clear()

    if x > size_max_X:
        x = size_max_X
        XV = XV * -1
    if x <= 0:
        x = 1
        XV = XV * -1

    YV += 0.411
    y += YV

    if y > size_max_y:
        y = size_max_y
        if YV > 0.5:
            YV = (YV/2) * -1
        else:
            YV = 0
    if y < 0:
        y = 1

    print(XV , " / " , YV)
    print("x", x," : y", y)
    print('vitesse du vent X' , VVX, "Y", VVY)

    if key.keyboard_pres()["a"]:
        paltau = pomme()


    co.afV2(paltau,round(x),round(y))
    time.sleep(0.063)
color.color.clear()

