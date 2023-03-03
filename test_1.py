import keyboard
from time import sleep

def clear():
    print( "\n" * 100 +"\033c")



key = {}
while_contucion = True
pas = 1
max_pas = 500

while while_contucion:
    if keyboard.is_pressed('a'):
        key["A"] = True
        pas = 0
    else:
        key["A"] = False

    if keyboard.is_pressed('b'):
        key["B"] = True
        pas = max_pas
    else:
        key["B"] = False


    if keyboard.is_pressed("right"):
        key["right"] = True
        pas += 1
    else:
        key["right"] = False

    if keyboard.is_pressed("left"):
        key["left"] = True
        pas += -1
    else:
        key["left"] = False


    if pas < 1:
        pas = 1
    if pas > max_pas:
        pas = max_pas


    if keyboard.is_pressed("q"):
        while_contucion = False

    if True in list(key.values()):
        pass
    else:
        pas = int(abs(pas / 10)) * 10

    new_pas = int(abs(pas / 10))
    new_max_pas = int(abs(max_pas / 10))
    pas_res = "NAN"
    pas_res = ("-" * new_pas +  "#" + "-" * (new_max_pas - new_pas) + " : ")
    clear()
    print(pas_res + " : " + str(key) + " : " + str(new_pas) + " " + str(pas), end="\n\n")
    sleep(0.01)

