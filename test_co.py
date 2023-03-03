import color
import copy
import time

from color import *

def creat_mat(size_X,size_Y):
    mat = []
    for y in range(0,size_Y):
        x_el = []
        for x in range(0,size_X):
            x_el.append("  ") #chr(0x1F333))
        mat.append(x_el)
    return mat

def afV2(mat, pos_x, pos_y):
    print("pos", pos_x,pos_y)
    matrice_af = copy.deepcopy(mat)
    if not 0 in [pos_x,pos_y]:
        matrice_af[pos_y - 1][pos_x - 1] = chr(9917) #chr(0x1F3E0)

    mure = color.set_color(115, 115, 115, True) + "  "

    srcin = ""
    for y_co,y_el in enumerate(matrice_af):
        x_contener = ""
        for x_co ,x_el in enumerate(y_el):
            x_contener += x_el
        srcin += (mure + color.set_color(11, 230, 222,True) + x_contener + mure + color.reset_color + "\n")

    print(srcin + str(color.set_color(112, 74, 28, True) + "  " * (len(mat[0]) + 2 ) + color.reset_color + "\r") * 2 )


def main():
    size_X, size_Y = int(input("size X >")) , int(input("Size Y >"))

    print(size_X, size_Y)

    matrice = creat_mat(size_X,size_Y)

    while_contision = True

    while while_contision:
        pozision_X , pozision_Y = int(input("pozision X >")), int(input("pozision Y >"))
        if -1 in [pozision_X,pozision_Y]:
            while_contision = False
        else:
            afV2(copy.deepcopy(matrice), pozision_X, pozision_Y)
def afV3(matrix,X,Y,Z):
    X_list = []
    for i in range(0,Z):
        X_list.append(matrix[X - (i - ( Z /2))])
    print(X_list)

if __name__ == "__main__":
    afV3([1,2,3,4,5,6,7,8,9,"#",11,12,13,14,15,16,17,18,19],10,0,4)