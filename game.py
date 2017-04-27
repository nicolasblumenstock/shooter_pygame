# ** -- the reason you have access to this module is because you ran $ pip install pygame -- **
# ** -- pygame is not part of core (like math or random is) -- **
import pygame
# ** -- Get sys module so we can exit game -- **
from random import randint
from Player import Player
from game_functions import *

# ** -- CORE GAME LOOP -- **
Red = randint(0, 255)
Green = randint(0, 255)
Blue = randint(0, 255)
frame = 0
def run_game():
	global frame
	# ** -- INIT ALL PYGAME STUFF -- **
	pygame.init()
	# ** -- set up a tuple for the screen size, horiz, vert -- **
	screen_size = (1000, 800)
	# ** -- setting background color with RGB -- **
	background_color = (Red, Green, Blue)
	# if (frame % 600 == 0):
	# 	background_color = (randint(0,255), randint(0,255), randint(0,255))
	# ** -- create screen size -- **
	screen = pygame.display.set_mode(screen_size)
	# **  -- set a caption on terminal window -- **
	pygame.display.set_caption("A Heroic 3rd Person Shooter")

	the_player = Player(screen)

# ** -- Main game loop. Run forever or until break -- **
	while 1:
		frame += 1
# ** -- Fill screen with background color -- **
		screen.fill(background_color)
		# snail_rave()	
		# ** -- the escape hatch (from while) -- **
		check_events()
		# clear the screen for the next time through the loop
		the_player.draw_me()
		pygame.display.flip()

run_game()