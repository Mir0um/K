import keyboard
touches_pressees = set()

    

# Définition d'une fonction appelée chaque fois qu'une touche est pressée
def on_press(event):
    # Imprime le nom de la touche pressée
    print(event.name)
    touches_pressees.add(event.name)
    print(sorted(list(touches_pressees)))

# Enregistrement de la fonction on_press() pour être appelée chaque fois qu'une touche est pressée
keyboard.on_press(on_press)

# Maintient le programme en cours d'exécution pour qu'il continue à imprimer les touches pressées
keyboard.wait()

