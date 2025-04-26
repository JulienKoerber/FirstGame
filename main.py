import pygame
import sys

# Initialiser pygame
pygame.init()

# Définir la taille de la fenêtre
LARGEUR_ECRAN = 600
HAUTEUR_ECRAN = 800
screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("Jeu d'esquive")

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

# Définir le joueur
joueur_largeur = 50
joueur_hauteur = 50
joueur_x = LARGEUR_ECRAN // 2 - joueur_largeur // 2
joueur_y = HAUTEUR_ECRAN - joueur_hauteur - 10
joueur_vitesse = 5

# Boucle principale du jeu
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # Limite à 60 images par seconde

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gérer les touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and joueur_x > 0:
        joueur_x -= joueur_vitesse
    if touches[pygame.K_RIGHT] and joueur_x < LARGEUR_ECRAN - joueur_largeur:
        joueur_x += joueur_vitesse

    # Dessiner
    screen.fill(BLANC)  # Fond blanc
    pygame.draw.rect(screen, ROUGE, (joueur_x, joueur_y, joueur_largeur, joueur_hauteur))  # Joueur
    pygame.display.flip()
