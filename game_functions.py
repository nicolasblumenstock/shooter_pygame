import pygame
import sys

def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
# ** -- the user clicked the red x. Get out of the loop and kill the game -- **
			sys.exit()

# def snail_rave():
# 	if (frame % 300 == 0):
# 		background_color = (randint(0,255), randint(0,255), randint(0,255))	