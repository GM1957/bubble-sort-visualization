import pygame
import time
import os
pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIGTH = 1000
current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'imgs') # The resource folder path
image_path = os.path.join(resource_path, 'pipe.png')# image path
PIPE_IMG = pygame.image.load(image_path)
# numbers = 

newnumbers = [40,60,20,80,10,69,44,30,90,23,57,75,26,78,34]
def showbubble(numbers=[],*args):
    win = pygame.display.set_mode((SCREEN_WIGTH,SCREEN_HEIGHT))
    time.sleep(1)
    l = 50
    for k in numbers:
        win.blit(PIPE_IMG, (l,(SCREEN_HEIGHT-(k*4))))
        pygame.display.update()   
        l = l+60

def main():
    clock = pygame.time.Clock()
    run = True
    startgame = False
    while run:
        win = pygame.display.set_mode((SCREEN_WIGTH,SCREEN_HEIGHT))
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startgame = True       
        # pygame.display.set_mode((SCREEN_WIGTH,SCREEN_HEIGHT))
        
        
        if startgame == False:
            j = 50
            for i in newnumbers:
                win.blit(PIPE_IMG, (j,(SCREEN_HEIGHT-(i*4))))
                pygame.display.update()   
                j = j+60
        if startgame == True:
            numbers = newnumbers
            for round in range(1,len(numbers)):
                for k in range(0,(len(numbers)-round)):
                    if(numbers[k]>numbers[k+1]):
                        temp = numbers[k]
                        numbers[k]= numbers[k+1]
                        numbers[k+1] = temp
                        print(numbers) 
                        showbubble(numbers)
                      
                    
                                          
main()