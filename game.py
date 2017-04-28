# ** -- the reason you have access to this module is because you ran $ pip install pygame -- **
# ** -- pygame is not part of core (like math or random is) -- **
import pygame
# ** -- Get sys module so we can exit game -- **
from Player import Player
from game_functions import *
from Enemy import Enemy
from pygame.sprite import Group, groupcollide

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

	the_player = Player(screen, './images/Hero.png', 100, 100)
	bad_dude = Enemy(screen)
	the_player_group = Group()
	the_player_group.add(the_player)
	enemies = Group()
	enemies.add(bad_dude)
	bullets = Group()



# ** -- Main game loop. Run forever or until break -- **
	while 1:
		frame += 1
		if (frame % 100 == 0):
			enemies.add(Enemy(screen))
# ** -- Fill screen with background color -- **
		screen.fill(background_color)
		if (frame % 3600 == 0):
			background_color = (randint(0,255), randint(0,255), randint(0,255))	
		# snail_rave(screen,frame,background_color)	
		# ** -- the escape hatch (from while) -- **
		check_events(screen,the_player,bullets)
		# clear the screen for the next time through the loop

		for player in the_player_group:
			the_player.draw_me()
		
		for bad_dude in enemies: 
			bad_dude.draw_me()
			bad_dude.update_me(the_player)

		# update and draw the bullets
		for bullet in bullets:
			bullet.draw_bullet()
			bullet.update()
	
		hero_died = groupcollide(the_player_group,enemies,True,False)
		bullet_death = groupcollide(bullets,enemies,True,True)

		pygame.display.flip()

run_game()