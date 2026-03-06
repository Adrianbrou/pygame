import pygame
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from logger import log_state

#this initialize the pygame
pygame.init()

#the entry point of our program
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #create a clock
    clock = pygame.time.Clock()
    dt = 0

    #create the infinite while loop
    while True:
        
        dt = clock.tick(60) / 1000
        

        log_state()
         
        for event in pygame.event.get():
            #this event help to close the game using the window
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        #call the clock object at the end and pass it 60 
        clock.tick(60)

if __name__ == "__main__":
    main()
