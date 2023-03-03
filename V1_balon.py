import copy
import functools
import random
import sys
import time


class color:
    reset_color = '\033[0m'

    def set_color(r, g, b, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    clear = ("\n" * 100 + "\033c")

class srcine():
    frame = ""

    def __init__(self, name:str, metode_afichage):
        self.name_srine = name
        self.srcine_metode_af = metode_afichage
        self.metode_af_name = str(metode_afichage)

    def aficher(self, text):
        func = functools.partial(self.srcine_metode_af, self)
        self.frame += list(map(func, [text]))[0]
        print(color.clear + self.frame)
        self.frame = ""

    def add_frame(self,txt):
        self.frame += str(txt) + "\n"

    def metode_af1(self,text):
        color1 = color.set_color(255,0,0,True)
        return color1 + text + color.reset_color + " M1 "

    def metode_af2(self,text):
        res = ""
        for i in text:
            res = i + res
        return color.set_color(62, 156, 0,True) + res + " M2" + color.reset_color

    def afV2(self,plat):

        res = ""
        for y in range(0, plat.size_y):
            acumulateur_x = ""
            for x in range(0,plat.size_X):
                acumulateur_x += str(plat.plateau_contenue[y][x]) + ","
            res += acumulateur_x[:-1] + "\n"
        return res

    def afV3(self,plateaus):

        plat = plateaus[0]
        color_plateau = plateaus[1]

        res = ""
        for y in range(0, color_plateau.size_y):
            acumulateur_x = ""
            for x in range(0,color_plateau.size_X):
                acumulateur_x += color.set_color(color_plateau.plateau_contenue[y][x][0],
                                                 color_plateau.plateau_contenue[y][x][1],
                                                 color_plateau.plateau_contenue[y][x][2],
                                                 True) + plat.plateau_contenue[y][x]
            res += acumulateur_x  + color.reset_color + "\n"
        return res


class obeject():
    position_x = 0
    position_Y = 0
    
    def __init__(self, name) -> None:
        self.name = name

class plateau():
    def __init__(self, name: str, sizeX:int = 0, sizeY:int = 0):
        self.name_palteau = name
        self.plateau_contenue = []
        self.size_X = sizeX
        self.size_y = sizeY

    def generate_random_num(self,max:int,min:int,size_X: int = 0, size_Y:int = 0):
        if 0 in [size_Y, size_X]:
            size_Y, size_X = self.size_y, self.size_X
        else:
            self.size_y, self.size_X = size_Y, size_X

        if not 0 in [size_Y,size_X]:
            mat = []
            for y in range(0, size_Y):
                x_el = []
                for x in range(0, size_X):
                    x_el.append(str(random.randint(min,max)))  # chr(0x1F333))
                mat.append(x_el)
            self.plateau_contenue = mat
        else:
            raise ValueError("Erreur : generation du plateau inposible car la taille est egale a 0")


    def generate_full_char(self, size_X:int = 0, size_Y:int = 0, char_de_ramplisage:str = "  "):
        if 0 in [size_Y,size_X]:
            size_Y, size_X = self.size_y, self.size_X
        else:
            self.size_y, self.size_X = size_Y, size_X

        if not 0 in [size_Y, size_X]:
            mat = []
            for y in range(0, size_Y):
                x_el = []
                for x in range(0, size_X):
                    x_el.append(char_de_ramplisage[0:2])  # chr(0x1F333))
                mat.append(x_el)
            self.plateau_contenue = mat
        else:
            raise ValueError("Erreur : generation du plateau inposible car la taille est egale a 0")
    def enumerai(self):
        for y in range(0,self.size_y):
            for x in range(0,self.size_y):
                self.plateau_contenue[y][x] = str(inverse_num(x,self.size_X)-1) + str(inverse_num(y,self.size_y)-1)

    def copy(self):
        return copy.deepcopy(self)


class phisic_paramaitre():
    pass

def inverse_num(nb,siz):
    return siz - nb


srine_1 = srcine("scr1",srcine.afV3)

plateau_1 = plateau("plt_1",135,67)

plateau_1.generate_full_char()
# ===================================
color_platau_1 = plateau("col_plat_1",plateau_1.size_X,plateau_1.size_y)

color_platau_1.generate_full_char()

color_platau_1_R = color_platau_1.copy()
color_platau_1_J = color_platau_1.copy()
color_platau_1_B = color_platau_1.copy()


while True:
    #plateau_1.generate_random_num(99,10,plateau_1.size_X,plateau_1.size_y)

    color_platau_1_R.generate_random_num(255,200)
    color_platau_1_J.generate_random_num(60,40)
    color_platau_1_B.generate_random_num(60,40)

    for y in range(0,color_platau_1.size_y):
        for x in range(0, color_platau_1.size_X):
            color_platau_1.plateau_contenue[y][x] = [color_platau_1_R.plateau_contenue[y][x],
                                                     color_platau_1_J.plateau_contenue[y][x],
                                                     color_platau_1_B.plateau_contenue[y][x]]


    srine_1.add_frame("test")
    srine_1.aficher([plateau_1,color_platau_1])

    time.sleep(0.025)
