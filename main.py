import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

disWidth = 600
disHeight = 400

dis = pygame.display.set_mode((disWidth, disHeight))
pygame.display.set_caption('Yılan Oyunu')

clock = pygame.time.Clock()

snakeBlock = 10
snakeSpeed = 15

fontStyle = pygame.font.SysFont("Tahoma", 25)
scoreFont = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = scoreFont.render("Puan: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snakeBlock, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeBlock, snakeBlock])


def message(msg, color):
    mesg = fontStyle.render(msg, True, color)
    dis.blit(mesg, [disWidth / 6, disHeight / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = disWidth / 2
    y1 = disHeight / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
    foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("tekar oynamak için \"C\", çıkmak için \"Q\"", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeBlock
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeBlock
                    x1_change = 0

        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snakeBlock, snakeBlock])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snakeBlock, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0
            foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


gameLoop()