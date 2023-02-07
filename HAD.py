import pygame
import random
import time
 
pygame.init()
 
dis_width = 1000 #600 
dis_height = 600 #400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('HAD')
 
clock = pygame.time.Clock()


 
snake_block = 10
snake_speed = 15
def our_snake(snake_block, snake_list):
    for body in snake_list:
        pygame.draw.rect(dis, "red", [body[0], body[1], snake_block, snake_block])

score_font = pygame.font.SysFont("bahnschrift", 30)
lose_font = pygame.font.SysFont("bahnschrift", 100)
 
 
hs = 0


def gameLoop():
    game_over = False
    game_close = True

    global hs

    snake_list = []
    snake_length = 0

    
    
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    foodx = int(round(random.randint(snake_block, dis_width - snake_block) / 10.0) * 10.0)
    foody = int(round(random.randint(snake_block, dis_height - snake_block) / 10.0) * 10.0)

    while not game_over:
        losing_text = lose_font.render("GAME OVER ", True, "red")
        text = score_font.render("Score : " + str(snake_length) , True, "yellow" )
        restart_text = score_font.render(" Press 'p' to play again!" , True, "red" )
        hscounter = score_font.render("Highscore : " + str(hs) , True, "yellow" )
        dis.blit(text, [0,0])
        dis.blit(hscounter, [(dis_width - 200),0])
        
        
 
        while game_close == False:
            dis.fill("blue")

            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    gameLoop()

 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            dis.blit(losing_text, [250, 250])
            dis.blit(restart_text, [350,400])
            x1 = 100000000
            y1 = 100000000
            if (snake_length) > hs:
                hs = (snake_length)
            

        x1 += x1_change
        y1 += y1_change

       
        pygame.draw.rect(dis, "red", [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, "green", [foodx, foody, snake_block, snake_block])
       
        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randint(snake_block, dis_width - snake_block) / 10.0) * 10.0)
            foody = int(round(random.randint(snake_block, dis_height - snake_block) / 10.0 ) * 10.0)
            print("mňam")
            snake_length = snake_length + 1


        if len(snake_list) > snake_length:
            del snake_list[0]


        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        our_snake(snake_block, snake_list)

        clock.tick(snake_speed)

        pygame.display.update()
        dis.fill("blue")
    pygame.quit()
    quit()
gameLoop()