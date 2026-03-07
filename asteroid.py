from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame,random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        """
        we always want to destroy the asteroids, Then according to the size it either respawn to more,or one more fast, or nothing
        """
        self.kill()
        #this case it is small size so no respawn
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            new_vector_1=self.velocity.rotate(rand_angle)
            new_vector_2=self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1,asteroid_2 = Asteroid(self.position.x,self.position.y,new_radius),Asteroid(self.position.x,self.position.y,new_radius)
            asteroid_1.velocity = new_vector_1 * 1.2
            asteroid_2.velocity = new_vector_2 * 1.2
        return 
