import pygame

pygame.init()
pygame.mixer.music.load('ex021music.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
