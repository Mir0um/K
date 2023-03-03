import pygame

def test1():
    # Initialisation de Pygame
    pygame.init()

    # Définition des couleurs
    ROUGE = (255, 0, 0)

    # Définition de la taille de la fenêtre
    taille_fenetre = (800, 600)

    # Création de la fenêtre
    fenetre = pygame.display.set_mode(taille_fenetre)

    # Titre de la fenêtre
    pygame.display.set_caption("Mon ballon")

    # Boucle principale
    terminer = False
    while not terminer:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                terminer = True

        # Effacer la fenêtre avec une couleur de fond
        fenetre.fill((255, 255, 255))

        # Dessiner un ballon rouge
        pygame.draw.circle(fenetre, ROUGE, (400, 300), 50)

        # Rafraîchir l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()

def test2():
    import pygame

    pygame.init()

    # définition des dimensions de la fenêtre
    screen_width = 800
    screen_height = 600

    # création de la fenêtre
    screen = pygame.display.set_mode((screen_width, screen_height))

    # définition de la couleur de fond
    background_color = (255, 255, 255)  # blanc

    # définition de la police et de la taille du texte
    font = pygame.font.Font(None, 36)

    # création du message texte
    text = font.render("Bonjour, Pygame !", True, (0, 0, 0))  # noir

    # boucle principale du programme
    running = True
    while running:
        # gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # affichage du fond
        screen.fill(background_color)

        # affichage du message texte
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))

        # rafraîchissement de l'affichage
        pygame.display.flip()

    pygame.quit()

def test3():

    pygame.init()

    # définition des dimensions de la fenêtre
    screen_width = 400
    screen_height = 300

    # création de la fenêtre
    screen = pygame.display.set_mode((screen_width, screen_height))

    # définition de la couleur de fond
    background_color = (255, 255, 255)  # blanc

    # définition des dimensions et de la position du rectangle
    rect_width = 50
    rect_height = 50
    rect_x = screen_width / 2 - rect_width / 2
    rect_y = screen_height / 2 - rect_height / 2

    # définition de la vitesse de déplacement
    move_speed = 5

    # boucle principale du programme
    running = True
    while running:
        # gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect_x -= move_speed
                elif event.key == pygame.K_RIGHT:
                    rect_x += move_speed
                elif event.key == pygame.K_UP:
                    rect_y -= move_speed
                elif event.key == pygame.K_DOWN:
                    rect_y += move_speed

        # affichage du fond
        screen.fill(background_color)

        # affichage du rectangle
        pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_width, rect_height))

        # rafraîchissement de l'affichage
        pygame.display.flip()

    pygame.quit()

test3()