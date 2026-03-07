import pygame,sys
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


#this initialize the pygame
pygame.init()

#the entry point of our program
def main():
    #variables to hold the position of the player on the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    """
    #######################################################################################################
                                            CEATION OF GROUPS
    
    """
    #player objects and groups
    updatable = pygame.sprite.Group() #object that can be update like player
    drawable = pygame.sprite.Group() #object that can be represent on the game like, triangle, circle..

    #creation of group of asteroids
    asteroids = pygame.sprite.Group()
    shots =  pygame.sprite.Group()

    """"
    ############################ STATIC CONTAINERS FIELDS ###########################################################################
    """

    #create now a container for its object 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable,shots)


    """"
    #######################################################################################################
    """
    #create a object(player/asteroidfield)
    player= Player(x,y)
    asteroid_field = AsteroidField()

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #here we set the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create a clock for the fps refresh
    clock = pygame.time.Clock()
    dt = 0

    #create the infinite while loop
    while True:
        log_state()
        
        for event in pygame.event.get():
            #this event help to close the game using the window
            if event.type == pygame.QUIT:
                return
        screen.fill("black")


        #collision check to kill asteroid
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    # asteroid.kill()
                    shot.kill()
        #collision check to die
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        


        #here we draw the player after filling the screen with black
        
        updatable.update(dt)

        for form in drawable:
            form.draw(screen)

        pygame.display.flip()
        #call the clock object at the end and pass it 60 
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
