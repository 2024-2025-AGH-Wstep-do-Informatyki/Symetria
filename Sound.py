import pygame

pygame.mixer.innit()

sound = mpygame.mixer.Sound("catch_sound2.mp3")

def play_sound():
  sound.play()

play_sound()
