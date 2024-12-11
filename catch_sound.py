import pygame

pygame.mixer.innit()

sound = mpygame.mixer.Sound("catch_sound.wav")

def play_sound():
  sound.play()

play_sound()
