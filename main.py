import pygame, sys

#Create Screen
WIDTH, HEIGHT = 1400, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

#Global
pygame.display.set_caption("Fruit Ninja")
BG = pygame.image.load("assets/background.jpeg")
SUBSCRIBE = pygame.image.load("assets/subscribe.png")
SUBSCRIBE = pygame.transform.scale(SUBSCRIBE, (700, 400))

#Fonts
pygame.font.init()
TITLE_FONT = pygame.font.Font('assets/Ninja Font.ttf', 55)

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def display():
    #Main Menu Display
    starting_title = TITLE_FONT.render("GAME NAME", False, RED)
    screen.blit(starting_title, (500, 100)) #x , y
    screen.blit(SUBSCRIBE, (375, 400))



def main(): 
    run = True #game is running
    start_game = False #game has not started
    
    while run: #Game window doesn't close
        clock.tick(FPS)
        for event in pygame.event.get(): #Get Events
            if event.type == pygame.QUIT: #Quit Event
                pygame.quit()
                run = False
                sys.exit()

        #update display
        display()
        pygame.display.update()


if __name__ == "__main__":
    main()