import pygame
import time
import random


pygame.init()


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)


display_width = 800
display_height = 600
block_size = 10


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('python snakeGame')
pygame.display.update()
clock = pygame.time.Clock()
FBS = 20
font = pygame.font.SysFont(None, 25)




def massage_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    
def scores(score, color):
    screen_score = font.render(score, True, color)
    gameDisplay.blit(screen_score, [(display_width/2)-block_size, display_height/2])

def snake(block_size, snakelist):
    for xny in snakelist:
        pygame.draw.rect(gameDisplay, black,[xny[0], xny[1], block_size, block_size])


def appleFood(randapplex, randappley, block_size):
    pygame.draw.rect(gameDisplay, red, [randapplex, randappley, block_size, block_size])


def gameLoop():
    gameExit = False
    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakelenght = 1
    
    randapplex = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randappley = round(random.randrange(0,display_height-block_size)/10.0)*10.0


    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            massage_to_screen("game over, you score: ", red)
            #scores(snakelenght, green)
            pygame.display.update()
            


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white)
        appleFood(randapplex, randappley, block_size)

        
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelenght:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True
                
        snake(block_size, snakelist)
        
        
        pygame.display.update()




        if lead_x == randapplex and lead_y == randappley:
            #print ("om om om")
            randapplex = round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randappley = round(random.randrange(0,display_height-block_size)/10.0)*10.0
            snakelenght += 1


        clock.tick(FBS)


    pygame.quit()
    quit()






gameLoop()
