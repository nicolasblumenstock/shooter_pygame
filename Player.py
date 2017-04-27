import pygame

class Player(object):
	def __init__(self,screen):
		self.image = pygame.image.load('./images/Hero.png')
		self.image = pygame.transform.scale(self.image, (207,250))
		self.x = 100
		self.y = 100
		self.screen = screen

	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])