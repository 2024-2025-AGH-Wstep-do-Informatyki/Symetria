import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Wczytanie tła
background = pygame.image.load("tło.png") 
background = pygame.transform.scale(background, (screen_width, screen_height))
