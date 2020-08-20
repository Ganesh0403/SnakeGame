import pygame as py
import random
import math
import os
# import time
from pygame import mixer

py.init()

# delay = 0.3

screen = py.display.set_mode((800,600))
py.display.set_caption("Snake Game")
icon = py.image.load("snake.png")
py.display.set_icon(icon)

black = (0,0,0)
clock = py.time.Clock()

score_value = 0

game_over = False

def gameloop():
    global game_over
    score_value = 0
    snakeX = 370
    snakeY = 480
    snake_size = 20
    snakeX_change = 0
    snakeY_change = 0
    textX = 10
    textY = 10
    fps = 30

    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", 'w') as f:
            f.write("0")

    with open("hiscore.txt", 'r') as f:
        hiscore = f.read()

    ballImg = py.image.load("circle.png")
    ballX = random.randint(0,768)
    ballY = random.randint(0,568)

    def ball(x, y):
        screen.blit(ballImg, (x,y))

    snk_list = []
    snk_length = 1

    def snake(screen, color, snk_list, snake_size):
    # screen.blit(snakeImg, (x,y))
        for x,y in snk_list:
            py.draw.rect(screen, color, [x, y, snake_size, snake_size])

    def iscollision(ballX, ballY, snakeX, snakeY):
        distance = math.sqrt(math.pow(ballX - snakeX, 2) + math.pow(ballY - snakeY, 2))
        if distance < 10:
            return True
        else: 
            return False

    font = py.font.Font("freesansbold.ttf",32)
    over_font = py.font.Font("freesansbold.ttf",32)

    def show_score( x, y):
        score = font.render(f"Score : {str(score_value)}  HighScore :  {hiscore}", True, (255, 255, 255))
        screen.blit(score, (x, y))

    game = False
    while not game_over:
        
        screen.fill((0,255,0))
        if game:
            s = over_font.render("Game Over! Press Enter key to Continue", True, (255, 255, 255))
            screen.blit(s, (100, 250))

            for event in py.event.get():
                if event.type == py.QUIT:
                    game_over = True
                if event.key == py.K_RETURN:
                        gameloop()
                
        else:    
            for event in py.event.get():
                if event.type == py.QUIT:
                    game_over = True
                if event.type == py.KEYDOWN:
                    if event.key == py.K_LEFT:
                        snakeX_change = -3
                        snakeY_change = 0
                    if event.key == py.K_RIGHT:
                        snakeX_change = 3
                        snakeY_change = 0
                    if event.key == py.K_UP:
                        snakeY_change = -3
                        snakeX_change = 0
                    if event.key == py.K_DOWN:
                        snakeY_change = 3
                        snakeX_change = 0

        snakeX += snakeX_change
        snakeY += snakeY_change
        
        collision = iscollision(ballX, ballY, snakeX, snakeY)
        if collision:
            ballX = random.randint(0,768)
            ballY = random.randint(0,568)
            mixer.music.load("beep1.mp3")
            mixer.music.play()
            score_value += 10
            snk_length += 10
            if score_value > int(hiscore):
                hiscore = score_value
        
        with open("hiscore.txt", 'w') as f:
            f.write(str(hiscore))

        head = []
        head.append(snakeX)
        head.append(snakeY)
        snk_list.append(head)

        if len(snk_list) > snk_length:
            del snk_list[0]

        if head in snk_list[ : -1]:
            ballX = 2000
            ballY = 2000
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            game = True

        if snakeX <= 0:
            ballX = 2000
            ballY = 2000
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            # snk_list.clear()
            game = True
        if snakeY <= 0:
            ballX = 2000
            ballY = 2000
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            # snk_list.clear()
            game = True
        if snakeX >= 790:
            ballX = 2000
            ballY = 2000
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            # snk_list.clear()
            game = True
        if snakeY >= 590:
            ballX = 2000
            ballY = 2000
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            # snk_list.clear()
            game = True

        snake(screen, black, snk_list, snake_size)
        ball(ballX, ballY) 
        show_score(textX, textY)   
        py.display.update()
        clock.tick(fps)
    # time.sleep(delay)
    py.quit()
    quit()
gameloop()