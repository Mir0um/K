import keyboard
import time
import color

def keyboard_pres():
    key_control = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'alt', 'b', 'backspace', 'c', 'ctrl', 'd', 'down', 'e', 'enter', 'esc', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'left', 'm', 'n', 'o', 'p', 'q', 'r', 'right', 's', 'shift', 'space', 't', 'u', 'up', 'v', 'w', 'x', 'y', 'z']
    key_control.sort()
    res = {}
    for k in key_control:
        res[k] = keyboard.is_pressed(k)
    return res

def main2():

    while not keyboard.is_pressed("esc"):
        color.color.clear()
        #print(keyboard_pres())
        print(keyboard_pres())
        print_ = "keboar key presed is:\n"
        for key , presed in keyboard_pres().items():
            if presed:
                print_ += str(key) + ","
        print(print_[:-1])
        time.sleep(0.05)

if __name__ == "__main__":
    main2()