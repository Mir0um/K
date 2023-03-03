import color
import test_co as co
import test_lis_test_printer as key
import keyboard
import time
import random

size_max = 40

size_X, size_Y = size_max,size_max

paltau = co.creat_mat(size_X,size_Y)

x = round(size_max/2)
y = round(size_max/2)

def pomme():
    paltau = co.creat_mat(size_X, size_Y)
    for i in range(1, 72):
        xpom = random.randint(0, size_max -1)
        ypom = random.randint(0, size_max -1)
        paltau[xpom][ypom] = chr(0x1F34E)
    return paltau

paltau = pomme()
while not keyboard.is_pressed("esc"):
    color.color.clear()
    print(key.keyboard_pres())
    if key.keyboard_pres()["right"]:
        x += 1
    if key.keyboard_pres()["left"]:
        x += -1

    if key.keyboard_pres()["down"]:
        y += 1
    if key.keyboard_pres()["up"]:
        y += -1

    if x > size_max:
        x = 1
    if x <= 0:
        x = size_max

    if y > size_max:
        y = 1
    if y <= 0:
        y = size_max

    if key.keyboard_pres()["a"]:
        paltau = pomme()


    co.afV2(paltau,round(x),round(y))
    time.sleep(0.063)
