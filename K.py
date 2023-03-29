import copy
import functools
import random
import num


class Color:
    """
    Cette gere touse qui conserne le couleure et le clrear de lecrand
    """

    #variable poure resete le code couleur
    reset_color = '\033[0m'
    

    def set_color(r:int = 0, g:int = 0, b:int = 0, background:bool = False):
        """
        Cette fonction calcule le code couleure.
        
        Args:
        r (int): couleur rouge de 0 a 255
        g (int): couleur jeaune de 0 a 255
        b (int): couleur bleu de 0 a 255
        background (int): aplique la couleur non pas au caracter de text mais au fond

        Returns:
        str: le code couleure pour le resse utiliser color.reset_color
        """
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

    #pour netoiler l'ecrande
    clear = ("\n" * 100 + "\033c")

class Screen():
    """
    cette class recroupe tout les fonction daffichage
    
    """

    head_frame = "" #a aficher aven la fonction d'affichage

    def __init__(self, name:str, metode_afichage):
        """
        inisialisation screen 

        Args:
        name (str): nom du screen
        metode_afichage (K.screen): quelle motode d'affichage utiliser
        """
        self.name_srine = name
        self.screen_metode_af = metode_afichage
        self.metode_af_name = str(metode_afichage)

    def aficher(self, text):
        """
        Cette fonction permet d'afficher du texte à l'écran en utilisant la méthode "screen_metode_af".
        Le texte à afficher doit être passé en argument "text".
        La méthode "screen_metode_af" est appelée avec l'objet "self" et le texte "text" en tant que paramètres.
        Le résultat est stocké dans la variable "self.head_frame", qui est ensuite affichée à l'écran avec la commande "print".
        Enfin, la variable "self.head_frame" est réinitialisée à une chaîne vide.
        """
        func = functools.partial(self.screen_metode_af, self)
        self.head_frame += list(map(func, [text]))[0]
        print(Color.clear + self.head_frame)
        self.head_frame = ""

    def add_head_frame(self,txt):
        """pour ajouter du contenu au header framme.
        le header framme est un espas avent le metode d'afichage"""
        self.head_frame += str(txt) + "\n"

    def af1(self,text):
        """afiche le text en rouge"""
        color1 = Color.set_color(255,0,0,True)
        return color1 + text + Color.reset_color

    def af_classic(self,plat):
        """
        aficher un plateau

        ex:
        screen1.aficher(plat)
        """

        long_max = len(str(max([max(map(int, sublist)) for sublist in plat.plateau_contenue])))

        print(long_max)

        def ralong(text,long):
            if len(str(text)) < long:
                return (" " * (long - len(str(text)))) + text
            else:
                return text

        res = ""
        for y in range(0, plat.size_y):
            acumulateur_x = ""
            for x in range(0,plat.size_X):
                acumulateur_x += ralong(str(plat.plateau_contenue[y][x]),long_max) + ","
            res += acumulateur_x[:-1] + "\n"
        return res

    def af_couleur(self,plateaus):
        """
        afiche un plateau en suiven les couleur d'un desimme plateau en 3 dimention de 2d.

        ex:
        plateau_1 en 2D classic
        color_platau_1 en a 3 dimension 2D R G et B 
        srine_1.aficher([plateau_1,color_platau_1])
        """

        plat = plateaus[0]
        color_plateau = plateaus[1]

        res = ""
        for y in range(0, color_plateau.size_y):
            acumulateur_x = ""
            for x in range(0,color_plateau.size_X):
                acumulateur_x += Color.set_color(color_plateau.plateau_contenue[y][x][0],
                                                 color_plateau.plateau_contenue[y][x][1],
                                                 color_plateau.plateau_contenue[y][x][2],
                                                 True) + plat.plateau_contenue[y][x]
            res += acumulateur_x  + Color.reset_color + "\n"
        return res


class Obeject():
    position = {"x":0,"y":0}
    size = {"x":0,"y":0}


    def __init__(self,name) -> None:
        self.name = name
        self.skin = "#"
        self.size = {"x":1,"y":1}
        

class Plateau():
    """
    pour crée et gerer des plateau
    """
    

    def __init__(self, name: str, sizeX:int = 0, sizeY:int = 0):
        """
        fonction inisialitation.

        Args:
        name (str): nom du tableau
        sizeX (int): taille du plateau selon lax X
        sizeY (int): taille du plateau selon lax Y
        """
        self.name_palteau = name
        self.plateau_contenue = []
        self.size_X = sizeX
        self.size_y = sizeY
        self.obeject_in_the_plateau = []

    def generate_random_num(self,max:int,min:int,size_X: int = 0, size_Y:int = 0):
        """
        generation de lespase du plateau avec des nombre aleatoir

        Args:
        max (int): valeur maximale
        min (int): valeur minimale
        sizeX (int): taille du plateau selon lax X
        sizeY (int): taille du plateau selon lax Y
        """
        
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
        """
        generation de lespase du plateau avec un carecter presie

        Args:
        sizeX (int): taille du plateau selon lax X
        sizeY (int): taille du plateau selon lax Y
        char_de_ramplisage (str): le caracter de text comme rempliseur
        """
        
        
        if size_Y == 0 or size_X == 0:
            size_Y, size_X = self.size_y, self.size_X
        else:
            self.size_y, self.size_X = size_Y, size_X

        if size_Y != 0 and size_X != 0:
            mat = [[char_de_ramplisage[0:2]] * size_X for _ in range(size_Y)]
            self.plateau_contenue = mat
        else:
            raise ValueError("Erreur : generation du plateau inposible car la taille est egale a 0")

        
    def enumerai(self,size_Y:int = 0,size_X:int = 0):
        """
        crée un plateau avec des case du plateau par ces coordoner
        """

        if 0 in [size_Y, size_X]:
            size_Y, size_X = self.size_y, self.size_X
        else:
            self.size_y, self.size_X = size_Y, size_X
        
        self.plateau_contenue =[[" "] * size_X for _ in range(size_Y)]

        for y in range(0,self.size_y):
            for x in range(0,self.size_X):
                self.plateau_contenue[y][x] = str(num.inverse_num(x,self.size_X)-1) + str(num.inverse_num(y,self.size_y)-1)

    def copy(self):
        """
        crée une copi du plateaux en inter conection
        """
        return copy.deepcopy(self)
    
    def ad_oblect(self,object:Obeject):
        self.obeject_in_the_plateau.append(object)
    
    def remov_oject(self,object:Obeject):
        self.obeject_in_the_plateau.remove(object)

    def name_des_object(self):
        res = []
        for i in self.obeject_in_the_plateau:
            res.append(i.name)
        return res