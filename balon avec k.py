import K
import time

srine_1 = K.srcine("scr1",K.srcine.afV3)

plateau_1 = K.plateau("plt_1",104,30)

plateau_1.generate_full_char()
# ===================================
color_platau_1 = K.plateau("col_plat_1",plateau_1.size_X,plateau_1.size_y)

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

    time.sleep(0.05)