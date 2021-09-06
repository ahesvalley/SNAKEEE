import pygame as pyg
import time
import random
pyg.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
colors = [white, yellow, black, red, green]


dis_width = 600
dis_height = 400
dis = pyg.display.set_mode((dis_width, dis_height))
pyg.display.set_caption('SNAKE The Game')

clock = pyg.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pyg.font.SysFont("bahnschrift", 25)
score_font = pyg.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list, save_color):
    y = -1
    for x in snake_list:
        pyg.draw.rect(dis, save_color[y], [x[0], x[1], snake_block, snake_block])
        y -= 1
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 10])

def drawfood(color_of_food, foodx, foody):
    pyg.draw.rect(dis, color_of_food, [foodx, foody, snake_block, snake_block])











def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []

    lenght_of_snake = 1

    foodx1 = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody1 = round(random.randrange(0, dis_height - snake_block) / 10) * 10
    foodx2 = round(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody2 = round(random.randrange(0, dis_height - snake_block) / 10) * 10
    colors = [white, yellow, black, red, green]
    color_of_food1 = colors[random.randrange(0, 2)]
    color_of_food2 = colors[random.randrange(0, 2)]
    save_color = [black]
    score = 0

    while not game_over:
        while game_close:
            dis.fill(white)
            message('Игра окончена, Нажми С играть заново или Q чтобы выйти', red)
            Your_score(score)
            pyg.display.update()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pyg.K_c:
                        gameLoop()


        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                game_over = True
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pyg.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pyg.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pyg.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)


        drawfood(color_of_food1, foodx1, foody1)
        drawfood(color_of_food2, foodx2, foody2)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(save_color) > 10:
            if save_color[-1] == save_color[-2] == save_color[-3]:
                del snake_List[-1]
                del snake_List[-1]
                del snake_List[-1]
                del save_color[-1]
                del save_color[-1]
                del save_color[-1]
                lenght_of_snake -= 3
        if len(snake_List) > lenght_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True


        our_snake(snake_block, snake_List, save_color)

        pyg.display.update()

        if x1 == foodx1 and y1 == foody1:
            foodx1 = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody1 = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            print('OMNOMNOM')
            lenght_of_snake += 1
            Your_score(score)
            score += 1
            save_color.append(color_of_food1)
            color_of_food1 = colors[random.randrange(0, 4)]
        elif x1 == foodx2 and y1 == foody2:
            foodx2 = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            foody2 = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            print('OMNOMNOM')
            lenght_of_snake += 1
            Your_score(score)
            score += 1
            save_color.append(color_of_food2)
            color_of_food2 = colors[random.randrange(0, 2)]


        clock.tick(snake_speed)

    pyg.quit()
    quit()
gameLoop()
