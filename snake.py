import pygame
import random
import time

pygame.font.init()

WIDTH,HEIGHT = 1000,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BG = (15,90,149)
pygame.display.set_caption('Snake game')
FPS = 60
SNAKE_STARTER_WIDTH = 20
SNAKE_STARTER_HEIGHT = 20

RECT = 40

GAMER_OVER_FONT = pygame.font.SysFont('comicsans',100)

def draw_window(grid,snake_length,obj):
    WIN.fill(BG)
    pygame.draw.rect(WIN, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), pygame.Rect(obj[1]*RECT, obj[0]*RECT, RECT, RECT)) #set column then row
    row = 0
    while row < HEIGHT/RECT:
        column = 0
        while column < WIDTH/RECT:
            pygame.draw.rect(WIN, (0,0,0), pygame.Rect(column*RECT, row*RECT, RECT, RECT),  2)
            column+=1
            
        row += 1

    x = 1
    while x <= snake_length:
        pygame.draw.rect(WIN, (0,100,0), pygame.Rect(grid[-x][1]*RECT, grid[-x][0]*RECT, RECT, RECT))
        x+=1

    pygame.display.update()

def movement(direction,grid):
    if direction == "right":
        val = grid[-1][1] +1            #coulmn
        grid.append([grid[-1][0],val])  

    elif direction == "left":
        val = grid[-1][1] -1
        grid.append([grid[-1][0],val])  

    elif direction == "down":
        val = grid[-1][0] +1 #row
        grid.append([val,grid[-1][1]])
    
    elif direction == "up":
        val = grid[-1][0] -1 #row
        grid.append([val,grid[-1][1]])


    
    

def random_obj():
    return (random.randint(0,(HEIGHT/RECT)-1),random.randint(0,(WIDTH/RECT)-1))    #We should use -1 because we woud run out of the canvas

def catch(grid,obj,snake_length):
    catched = False
    if grid[-1][0] == obj[0] and grid[-1][1] == obj[1]:
        snake_length +=1
        catched = True
    return snake_length,catched

def game_over(grid,snake_length):
    if grid[-1][0] < 0 or grid[-1][1] < 0 or grid[-1][0] > 14 or grid[-1][1] > 24:
        draw_game_over("Game over!")
    x = 2
    while x <= snake_length:
        print("utolso:" + str(grid[-1][0]) +" "+ str(grid[-1][1]))
        print("tobbi:" + str(grid[-x][0]) +" "+ str(grid[-x][1]))
        if grid[-1][0] == grid[-x][0] and grid[-1][1] == grid[-x][1]:
            draw_game_over("Game over!")


        x+=1

def draw_game_over(text):
    draw_text = GAMER_OVER_FONT.render(text,1,(255,255,255))
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(1000)
    main()

def main():
    run = True
    
    clock = pygame.time.Clock()
    direction = "right"
    grid = [[0,0]]
    snake_length = 2
    obj = random_obj()
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
   
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_RIGHT:
                    if direction != "left":
                        direction = "right"
                elif event.key == pygame.K_LEFT:
                    if direction != "right":
                        direction = "left"
                elif event.key == pygame.K_DOWN:
                    if direction != "up":
                        direction = "down"
                elif event.key == pygame.K_UP:
                    if direction != "down":
                        direction = "up"

                
                    

        movement(direction,grid)
        
        result = catch(grid,obj,snake_length)
        snake_length = result[0]
        if result[1] == True:
            obj = random_obj()
        game_over(grid,snake_length)
        draw_window(grid,snake_length,obj)
        time.sleep(0.2)

if __name__ == '__main__':
    main()