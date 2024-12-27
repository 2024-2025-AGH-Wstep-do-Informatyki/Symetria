import pygame
pygame.mixer.innit()
sound = mpygame.mixer.Sound("catch_sound1.mp3")

def play_sound():
  sound.play()

play_sound()
