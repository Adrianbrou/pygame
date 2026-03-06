import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state
from player import Player

#this initialize the pygame
pygame.init()

#the entry point of our program
def main():
    #variables to hold the position of the player on the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    #player object
    player = Player(x,y)
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
        #here we draw the player after filling the screen with black
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
        #call the clock object at the end and pass it 60 
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
