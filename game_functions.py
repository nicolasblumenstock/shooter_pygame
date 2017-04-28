import pygame
import sys
from random import randint
from Bullet import Bullet

pressed_down = {
	'up': False,
	'down': False,
	'left': False,
	'right': False
}
def check_events(screen,the_player,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
# ** -- the user clicked the red x. Get out of the loop and kill the game -- **
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up", True)
			elif event.key == 274:
				the_player.should_move('down', True)
			elif event.key == 275:
				the_player.should_move('right', True)
			elif event.key == 276:
				the_player.should_move('left', True)
			elif event.key == 121:
				the_player.x = 100
				the_player.y = 100
			elif event.key == 32:
				# user pressed the space bar to fire
				for direction in range (1,5):
					new_bullet = Bullet(screen,the_player,direction)
					bullets.add(new_bullet)

		elif event.type == pygame.KEYUP:
			if event.key == 273:
				the_player.should_move("up", False)
			if event.key == 274:
				the_player.should_move("down", False)
			if event.key == 275:
				the_player.should_move("right", False)
			if event.key == 276:
				the_player.should_move("left", False)

			# elif event.key == 121:
			# 	hero['x'] = 100
			# 	hero['y'] = 100
			# elif event.key == 32:
			# 	game_paused = not game_paused

# def snail_rave(screen,frame,background_color):
