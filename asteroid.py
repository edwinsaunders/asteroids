import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "0xFFFFFF", self.position, self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		#velocity vectors for two new asteroids
		vel1 = self.velocity.rotate(random_angle)
		vel2 = self.velocity.rotate(-random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		# create two new asteroids at this pos
		ast1 = Asteroid(self.position.x, self.position.y, new_radius)
		ast2 = Asteroid(self.position.x, self.position.y, new_radius)
		ast1.velocity = vel1 * 1.2
		ast2.velocity = vel2 * 1.2
