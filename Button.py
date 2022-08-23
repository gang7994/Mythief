import pygame
class Button():
	def __init__(self, image0, image1, pos, scale_x, scale_y):
		self.image0 = pygame.transform.scale(image0, (scale_x, scale_y))
		self.image1 = pygame.transform.scale(image1, (scale_x, scale_y))
		self.image = self.image0
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.rect_width = self.rect.size[0]
		self.rectr_height = self.rect.size[1]
  

	def update(self, screen):
		screen.blit(self.image, self.rect)


	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = self.image1
		else:
			self.image = self.image0