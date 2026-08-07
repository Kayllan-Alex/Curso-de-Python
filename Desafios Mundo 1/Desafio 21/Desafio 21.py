import pygame
import os
pygame.mixer.init()
arquivo = os.path.join(os.path.dirname(__file__), "Heaven Knows I'm Miserable Now.mpeg")
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()
input("Pressione ENTER para parar...")
pygame.mixer.music.stop()
# Fiz uma pesquisa de como fazer.