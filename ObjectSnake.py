import pygame as pyg
import time
import random
import math
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

font_style = pyg.font.SysFont("bahnschrift", 18)
score_font = pyg.font.SysFont("comicsansms", 35)

def Your_score(score):
    """Функция, показывающая счет( вывод через render)"""
    value = score_font.render("Your Score: " + str(score), True, red)
    dis.blit(value, [0, 0])

#def our_snake(snake_block, snake_list, save_color):
    #y = -1
    #for x in snake_list:
    #    pyg.draw.rect(dis, save_color[y], [x[0], x[1], snake_block, snake_block])
    #    y -= 1
def message(msg, color):
    """Функция для отображения сообщения ( вывод через render)"""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 10, dis_height / 10])

#def drawfood(color_of_food, foodx, foody):
    #pyg.draw.rect(dis, color_of_food, [foodx, foody, snake_block, snake_block])

class Food():
    """Класс еды, где даны начальные координаты и цвет"""
    x = 0
    y = 0
    color_of_food = red

    def __init__(self):
        """Основная функция, которая вызывается при обращению к классу"""
        self.regenerate()
    def regenerate(self):
        """Функция задания рандомных координат в пределах экрана ирандомного цвета в пределах списка"""
        self.x = round(random.randrange(0, dis_width - snake_block) / 10) * 10
        self.y = round(random.randrange(0, dis_height - snake_block) / 10) * 10
        self.color_of_food = random.choice(colors)
    def drawfood(self):
        """Функция отрисовки прямугольной еды, обращаясь к собственным данным класса"""
        pyg.draw.rect(dis, self.color_of_food, [self.x, self.y, snake_block, snake_block])
    def coordinats(self):
        summ = self.x + self.y
        return summ

class Snake():
    """Класс, отвечающий за змею,

    где даны начальные координаты, цвет первого блока в списке, список координат всего тела змеи,
    ее длина и координаты головы

    """
    x1 = dis_width / 2
    y1 = dis_height / 2
    save_color = [black]
    list = []
    lenght = 1
    head = []
    x1_change = 0
    y1_change = 0

    def creation(self):
        """Функция прорисовки змеи, цикл идет по всем координатам списка

        и задает определенный цвет прямугольника
        список координат также является списком из двух элементов, где х - первый элемент, у - второй

        """
        count = -1
        for x in self.list:
            pyg.draw.rect(dis, self.save_color[count], [x[0], x[1], snake_block, snake_block])
            count -= 1
    def control(self, x1_change, y1_change):
        """Функция управления змеей с привлеченим сторонних переменных, не входящих в класс"""
        self.x1 += x1_change
        self.y1 += y1_change
    def crash(self):
        """Функция выхода змеи за пределы дисплея, условие проигрыша"""
        if self.x1 >= dis_width or self.x1 < 0 or self.y1 >= dis_height or self.y1 < 0:
            Menu.game_close = True
    def move(self):
        """Функция составления списков змеи.

        В список головы добавляются два элемента с координатами блока,
        список головы - список отвечающий за блок головы змеи
        Далее формируется список всей змеи и если список больше длины змеи,
        удаляется первый элемент списка, чтобы змея не оставляла "следы"

        """
        self.head = []
        self.head.append(self.x1)
        self.head.append(self.y1)
        self.list.append(self.head)
        if len(self.list) > self.lenght:
            del self.list[0]
    def eat_tale(self):
        """Функция - условие проигрыша. Цикл сопоставляет координаты тела змеи с головой. Совпадение - проигрыш"""
        for x in self.list[:-1]:
           if x == self.head:
              Menu.game_close = True
    def eat_dish(self):
        ''' поедание еды, увеличение хвота'''
        self.lenght += 1
    def tetris(self):
        """Функция удаления трех блоков тела змеи, если их цвета совпадают"""
        if (len(self.save_color)) > 5:
            if self.save_color[-1] == self.save_color[-2] == self.save_color[-3]:
                del self.list[-1]
                del self.list[-1]
                del self.list[-1]
                del self.save_color[-1]
                del self.save_color[-1]
                del self.save_color[-1]
                self.lenght -= 3
    def reset(self):
        """Функция обнуления данных для новой игры"""
        self.save_color = [black]
        self.list = []
        self.lenght = 1
        self.head = []
    '''def choose_way(self):
        print('choose')
        if math.fabs(self.x1 - Food.x) < math.fabs(self.y1 - Food.y):
            if (self.x1 - Food.x) == 0:
                self.way_y()
            else:
                self.way_x()
        else:
            if self.y1 - Food.y == 0:
                self.way_x()
            else:
                self.way_y()'''

    '''def way_x(self):
        print('x')
        if (self.x1 - Food.x) > 0:
            self.x1_change = -10
            self.y1_change = 0
        elif (self.x1 - Food.x) < 0:
            self.x1_change = 10
            self.y1_change = 0
        else:
            self.way_y()
    def way_y(self):
        print('y')
        if (self.y1 - Food.y) > 0:
            self.x1_change = 0
            self.y1_change = -10
        elif (self.y1 - Food.y) < 0:
            self.x1_change = 0
            self.y1_change = 10
        else:
            self.way_x()'''
class Menu():
    """Класс для основных условий игры. Меню и Выход. Сделал для обращению к переменным из других классов"""
    game_over = False
    game_close = False


def gameLoop():
    """Основная функция игрового процесса, даются начальные данные, классы превязываются к переменным"""
    Menu.game_over = False
    Menu.game_close = False
    """змея неподвижна"""
    snake = Snake()
    snake.reset()
    x1_change = 0
    y1_change = 0
    food_number = 2
    foods = [Food() for i in range(food_number)]
    food1 = foods[0]
    food2 = foods[1]
    choosen_foodx = 0
    choosen_foody = 0
    """с помощью класса создается два объекта еды"""
    score = 0
    while not Menu.game_over:
        while Menu.game_close:
            """Режим паузы, экран белый, вывод сообщения, 
            
            при помощи библиотеки pygame создается условия выхода или перезапуска
            
            """
            dis.fill(white)
            message('Игра окончена, Нажми С играть заново или Q чтобы выйти', red)
            Your_score(score)
            pyg.display.update()
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    Menu.game_over = True
                    Menu.game_close = False
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_q:
                        Menu.game_over = True
                        Menu.game_close = False
                    if event.key == pyg.K_c:
                        gameLoop()
        for event in pyg.event.get():
            """в условии запущенной игры, при помощи библиотеки pygame переменным изменения координат 
            
            присваиваются новые данные
            
            """
            if event.type == pyg.QUIT:
                Menu.game_over = True
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
        if math.fabs((snake.x1 + snake.y1) - (food1.x + food1.y)) <= math.fabs((snake.x1 + snake.y1) - (food2.x + food2.y)):
            choosen_foodx = food1.x
            choosen_foody = food1.y
        else:
            choosen_foodx = food2.x
            choosen_foody = food2.y
        if math.fabs(snake.x1 - choosen_foodx) < math.fabs(snake.y1 - choosen_foody):
            if (snake.x1 - choosen_foodx) == 0:
                if (snake.y1 - choosen_foody) > 0:
                    if y1_change == 10:
                        if snake.x1 < choosen_foodx:
                            x1_change = 10
                            y1_change = 0
                        else:
                            x1_change = -10
                            y1_change = 0
                    else:
                        x1_change = 0
                        y1_change = -10
                elif (snake.y1 - choosen_foody) < 0:
                    if y1_change == -10:
                        if snake.x1 < choosen_foodx:
                            x1_change = 10
                            y1_change = 0
                        else:
                            x1_change = -10
                            y1_change = 0
                    else:
                        x1_change = 0
                        y1_change = 10
            else:
                if (snake.x1 - choosen_foodx) > 0:
                    if x1_change == 10:
                        if snake.y1 < choosen_foody:
                            x1_change = 0
                            y1_change = 10
                        else:
                            x1_change = 0
                            y1_change = -10
                    else:
                        x1_change = -10
                        y1_change = 0
                elif (snake.x1 - choosen_foodx) < 0:
                    if x1_change == -10:
                        if snake.y1 < choosen_foody:
                            x1_change = 0
                            y1_change = 10
                        else:
                            x1_change = 0
                            y1_change = -10
                    else:
                        x1_change = 10
                        y1_change = 0
        else:
            if snake.y1 - choosen_foody == 0:
                if (snake.x1 - choosen_foodx) > 0:
                    if x1_change == 10:
                        if snake.y1 < choosen_foody:
                            x1_change = 0
                            y1_change = 10
                        else:
                            x1_change = 0
                            y1_change = -10
                    else:
                        x1_change = -10
                        y1_change = 0
                elif (snake.x1 - choosen_foodx) < 0:
                    if x1_change == -10:
                        if snake.y1 < choosen_foody:
                            x1_change = 0
                            y1_change = 10
                        else:
                            x1_change = 0
                            y1_change = -10
                    else:
                        x1_change = 10
                        y1_change = 0
            else:
                if (snake.y1 - choosen_foody) > 0:
                    if y1_change == 10:
                        if snake.x1 < choosen_foodx:
                            x1_change = 10
                            y1_change = 0
                        else:
                            x1_change = -10
                            y1_change = 0
                    else:
                        x1_change = 0
                        y1_change = -10
                elif (snake.y1 - choosen_foody) < 0:
                    if y1_change == -10:
                        if snake.x1 < choosen_foodx:
                            x1_change = 10
                            y1_change = 0
                        else:
                            x1_change = -10
                            y1_change = 0
                    else:
                        x1_change = 0
                        y1_change = 10

        """обращением к классам и выполнение их функций, дисплей обновляется по скорости змеи (fps)"""
        snake.crash()
        snake.control(x1_change, y1_change)
        dis.fill(blue)
        food1.drawfood()
        food2.drawfood()
        snake.move()
        snake.eat_tale()
        snake.tetris()
        snake.creation()
        pyg.display.update()


        if food1.x == snake.x1 and food1.y == snake.y1:
            """условие поедания еды, выполнение функций классов"""
            snake.save_color.append(food1.color_of_food)
            food1.regenerate()
            snake.eat_dish()
            print('OMNOMNOM')
            print(snake.x1, snake.y1,)
            print(food1.x, food1.y)
            Your_score(score)
            score += 1
        elif food2.x == snake.x1 and food2.y == snake.y1:
            snake.save_color.append(food2.color_of_food)
            food2.regenerate()
            snake.eat_dish()
            print('OMNOMNOM')
            Your_score(score)
            score += 1
        clock.tick(snake_speed)

    pyg.quit()
    quit()
gameLoop()
