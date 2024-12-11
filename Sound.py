import pygame

pygame.mixer.innit()

sound = mpygame.mixer.Sound("catch_sound.mp3")

def play_sound():
  sound.play()

play_sound()
