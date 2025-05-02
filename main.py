import pygame
import sys
import random

# Initialiser pygame
pygame.init()

# Définir la taille de la fenêtre
LARGEUR_ECRAN = 600
HAUTEUR_ECRAN = 800
screen = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("Jeu d'esquive")

# Charger l'image de fond
background_image = pygame.image.load("images/eric.png")
background_image = pygame.transform.scale(background_image, (LARGEUR_ECRAN, HAUTEUR_ECRAN))

# Définir le joueur
joueur_largeur = 70
joueur_hauteur = 100
joueur_x = LARGEUR_ECRAN // 2 - joueur_largeur // 2
joueur_y = HAUTEUR_ECRAN - joueur_hauteur - 10
joueur_vitesse = 5

# Charger l'image du joueur
joueur_image = pygame.image.load("images/val.png")
joueur_image = pygame.transform.scale(joueur_image, (joueur_largeur, joueur_hauteur))

# Définir les objets à esquiver
objets = []
objet_largeur = 70
objet_hauteur = 100
objet_vitesse = 5

# Charger l'image des objets
objet_image = pygame.image.load("images/marius.png")
objet_image = pygame.transform.scale(objet_image, (objet_largeur, objet_hauteur))

# Charger une police pour le texte
font = pygame.font.SysFont(None, 75)

# Fonction pour ajouter un nouvel objet
def ajouter_objet():
    x = random.randint(0, LARGEUR_ECRAN - objet_largeur)
    y = -objet_hauteur
    objets.append([x, y])

# Fonction pour afficher un message
def afficher_message(message):
    texte = font.render(message, True, (255, 0, 0))  # Texte rouge
    texte_rect = texte.get_rect(center=(LARGEUR_ECRAN // 2, HAUTEUR_ECRAN // 2))
    screen.blit(texte, texte_rect)
    pygame.display.flip()
    pygame.time.wait(1000)  # Attendre 1 seconde
    pygame.quit()
    sys.exit()

# Boucle principale du jeu
clock = pygame.time.Clock()
compteur = 0  # Compteur pour ajouter des objets périodiquement

running = True
while running:
    clock.tick(60)  # Limite à 60 images par seconde
    compteur += 1

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

    # Ajouter un nouvel objet toutes les 60 frames
    if compteur % 60 == 0:
        ajouter_objet()

    # Déplacer les objets
    for objet in objets:
        objet[1] += objet_vitesse

    # Vérifier les collisions
    for objet in objets:
        if (joueur_x < objet[0] + objet_largeur and
            joueur_x + joueur_largeur > objet[0] and
            joueur_y < objet[1] + objet_hauteur and
            joueur_y + joueur_hauteur > objet[1]):
            afficher_message("You Loose")

    # Supprimer les objets hors de l'écran
    objets = [objet for objet in objets if objet[1] < HAUTEUR_ECRAN]

    # Dessiner
    screen.blit(background_image, (0, 0))  # Afficher l'image de fond
    screen.blit(joueur_image, (joueur_x, joueur_y))  # Afficher l'image du joueur
    for objet in objets:
        screen.blit(objet_image, (objet[0], objet[1]))  # Afficher les images des objets
    pygame.display.flip()