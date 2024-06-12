import os
# ~/.bash_login file.
import pika
import pygame
import  sys
mainClock = pygame.time.Clock()
from pygame.locals import *
import random
from enum import Enum
from pygame import mixer
import time

pygame.init()
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((500, 500))
pygame.font.init()
# font = pygame.font.SysFont(None, 30) 

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
color_box = BLUE
background = GRAY
font = pygame.font.SysFont(None, 48)
# img = font.render('123', True, RED)

# rect = img.get_rect()
# rect.topleft = (20, 20)


def draw_text_menu(text, font, color, surface, x, y):
    global textobj
    textobj = font.render(text, True, (0, 0, 0))
    global textrect
    textrect = textobj.get_rect()

    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    # surface.blit(font.render(textobj, True, (255, 0, 0)), (200, 100))

    # img = font.render(sysfont, True, RED)
    # rect = img.get_rect()
    # pygame.draw.rect(img, BLUE, rect, 1)
    #
    # font1 = pygame.font.SysFont('chalkduster.ttf', 72)
    # img1 = font1.render('chalkduster.ttf', True, BLUE)
    #
    # screen.fill(background)
    # screen.blit(img, (20, 20))



# def draw_text_button(text, font, color, surface, x, y):
#     textobj = font.render(text, 1, color, color)
#     textrect = textobj.get_rect()
#     textrect.center = (x, y)
    # textrect.blit(textobj, textrect)
    # surface.blit(font.render(textobj, True, (255, 0, 0)), (200, 100))





def main_menu():
    click = False
    run = True
    while run:

        screen.fill(background)

        draw_text_menu('Menu - Tank Game', font, (255, 255, 255), screen, 20, 20)
        draw_text_menu('<- Single Player', font, (0, 255, 0), screen, 240, 100)
        draw_text_menu('<- MultiPlayer', font, (0, 255, 0), screen, 240, 200)
        draw_text_menu('<- QUIT', font, (0, 255, 0), screen, 240, 310)


        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(30, 100, 200, 50)
        button_2 = pygame.Rect(30, 200, 200, 50)
        button_3 = pygame.Rect(30, 300, 200, 50)

        surf = pygame.Surface((200, 200))
        surf.fill((220, 200, 0))  #

        # rect_button = button_1.get_rect(35, 100)

        # if button_1.collidepoint((mx, my)):
        #     pygame.draw.rect(screen, (255, 0, 0), button_1)

        surface_change = pygame.Surface((200, 50))
        surface_change.fill(RED)

        if button_1.collidepoint((mx, my)):
            screen.blit(surface_change, (20, 100))
            screen.blit(surface_change, (20, 110))
            screen.blit(surface_change, (20, 90))
            screen.blit(surface_change, (40, 100))
            screen.blit(surface_change, (40, 110))
            screen.blit(surface_change, (40, 90))
            if click:
                os.system("python3 single.py")
        color_box = BLUE
        if button_2.collidepoint((mx, my)):
            screen.blit(surface_change, (20, 200))
            screen.blit(surface_change, (20, 210))
            screen.blit(surface_change, (20, 190))
            screen.blit(surface_change, (40, 200))
            screen.blit(surface_change, (40, 210))
            screen.blit(surface_change, (40, 190))
            if click:
                os.system("python3 multiple.py")
        if button_3.collidepoint((mx, my)):
            screen.blit(surface_change, (20, 300))
            screen.blit(surface_change, (20, 310))
            screen.blit(surface_change, (20, 290))
            screen.blit(surface_change, (40, 300))
            screen.blit(surface_change, (40, 310))
            screen.blit(surface_change, (40, 290))
            if click:
                run = False
                pygame.quit()


        pygame.draw.rect(screen, color_box, button_1)
        pygame.draw.rect(screen, color_box, button_2)
        pygame.draw.rect(screen, color_box, button_3)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True



        screen.blit(textobj, textrect)

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill(background)

        # draw_text('Single Player', font, (0, 255, 0), screen, 25, 50)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))

        # draw_text('MultiPlayer', font, (0, 255, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()

##################################### SinglePlayer ####################################



pygame.init()
pygame.display.set_caption("Single Tank Game")
screen = pygame.display.set_mode((800, 600))


bg = pygame.image.load(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\felt_green.jpg')

# mixer.music.load(r"C:\games\Tank\mus\1.wav")  # скачать другую постоянную песню
# mixer.music.play(-1)

move_sound = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\move_Sound.wav')
move_sound.set_volume(0.01)
Gameover_sound = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\gameover_sound.ogg')
fire = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\fire_sound.wav')
fire.set_volume(0.02)
explosion = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\explotion_sound.wav')
explosion.set_volume(0.02)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class shot(Enum):
    SHOT = 1


class Tank:

    def __init__(self, imagename, Place_x, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP,
                 d_down=pygame.K_DOWN):
        self.x = random.randint(200, 600)
        self.y = random.randint(200, 400)
        self.Place_x = Place_x
        self.speed = 2
        self.width = 50
        self.health_amount = 3
        self.direction = Direction.RIGHT
        self.KEYS = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                     d_up: Direction.UP, d_down: Direction.DOWN}
        self.tank_image = pygame.image.load(imagename)
        self.tank_image_static = self.tank_image

    def draw(self):
        screen.blit(self.tank_image_static, (self.x, self.y))
        return self.x, self.y

    def Change_dir(self, direction):
        self.direction = direction

    # def random_pos(self):
    #     self.x = random.randint(200, 600)
    #     self.y = random.randint(200, 400)

    def health_of_tank(self):
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Health: " + str(self.health_amount), 1, (0, 0, 0))
        place = text.get_rect(center=(self.Place_x, 50))
        screen.blit(text, place)

    def move(self):
        if self.direction == Direction.RIGHT:
            self.tank_image_static = pygame.transform.rotate(self.tank_image, -90)
            self.x += self.speed
        if self.direction == Direction.LEFT:
            self.tank_image_static = pygame.transform.rotate(self.tank_image, 90)
            self.x -= self.speed
        if self.direction == Direction.UP:
            self.tank_image_static = pygame.transform.rotate(self.tank_image, 0)
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.tank_image_static = pygame.transform.rotate(self.tank_image, 180)
            self.y += self.speed

        if self.x > screen.get_size()[0]:
            self.x = 0 - self.width
        if self.x < 0 - self.width:
            self.x = screen.get_size()[0]
        if self.y > screen.get_size()[1]:
            self.y = 0 - self.width
        if self.y < 0 - self.width:
            self.y = screen.get_size()[1]

        self.draw()


class Bullet:
    def __init__(self, tank, shoot=pygame.K_RETURN):
        self.bullet_x = -100
        self.bullet_y = -100
        self.bullet_speed = 15
        self.tank = tank
        self.bullet_width = 16
        self.bullet_height = 4
        self.radius = 3
        self.fire_yes = False
        self.direction = Direction.RIGHT
        self.color = (255, 0, 0)

        self.KEYS = {shoot: shot.SHOT}

    def bullet_pos(self):
        if self.direction == Direction.RIGHT and self.fire_yes == False:
            self.bullet_x = self.tank.x + self.tank.width + 16 // 2
            self.bullet_y = self.tank.y + 16 // 2
            self.bullet_width = 20
            self.bullet_height = 4
        if self.direction == Direction.LEFT and self.fire_yes == False:
            self.bullet_x = self.tank.x - 16 // 2
            self.bullet_y = self.tank.y + 16 // 2
            self.bullet_width = 20
            self.bullet_height = 4
        if self.direction == Direction.UP and self.fire_yes == False:
            self.bullet_x = self.tank.x + 16 // 2
            self.bullet_y = self.tank.y - 16 // 2
            self.bullet_width = 4
            self.bullet_height = 20
        if self.direction == Direction.DOWN and self.fire_yes == False:
            self.bullet_x = self.tank.x + 16 // 2
            self.bullet_y = self.tank.y + self.tank.width + 16 // 2
            self.bullet_width = 4
            self.bullet_height = 20

    def draw_bullet(self):
        if self.fire_yes:
            if self.direction == Direction.RIGHT:
                pygame.draw.circle(screen, self.color,
                                   (self.bullet_x, self.bullet_y), self.radius)
            if self.direction == Direction.LEFT:
                pygame.draw.circle(screen, self.color,
                                   (self.bullet_x, self.bullet_y), self.radius)
            if self.direction == Direction.UP:
                pygame.draw.circle(screen, self.color,
                                   (self.bullet_x, self.bullet_y), self.radius)
            if self.direction == Direction.DOWN:
                pygame.draw.circle(screen, self.color,
                                   (self.bullet_x, self.bullet_y), self.radius)

    def fire_false(self):
        if self.bullet_x >= screen.get_size()[0]:
            self.fire_yes = False
        if self.bullet_x <= 0:
            self.fire_yes = False
        if self.bullet_y >= screen.get_size()[1]:
            self.fire_yes = False
        if self.bullet_y <= 0:
            self.fire_yes = False

    def direction_bullet(self):
        if self.fire_yes == False:
            if self.tank.direction == Direction.RIGHT:
                self.direction = Direction.RIGHT
            if self.tank.direction == Direction.LEFT:
                self.direction = Direction.LEFT
            if self.tank.direction == Direction.UP:
                self.direction = Direction.UP
            if self.tank.direction == Direction.DOWN:
                self.direction = Direction.DOWN

    def move_bullet(self):
        if self.direction == Direction.RIGHT:
            self.bullet_x += self.bullet_speed
        if self.direction == Direction.LEFT:
            self.bullet_x -= self.bullet_speed
        if self.direction == Direction.UP:
            self.bullet_y -= self.bullet_speed
        if self.direction == Direction.DOWN:
            self.bullet_y += self.bullet_speed

        self.draw_bullet()
        self.direction_bullet()
        self.fire_false()

    def collision_tank(self, tank_enemy):
        left_x1 = self.bullet_x
        left_x2 = tank_enemy.x
        right_x1 = self.bullet_x + self.bullet_width
        right_x2 = tank_enemy.x + tank_enemy.width
        bullet_y1 = self.bullet_y
        tankenemy_y2 = tank_enemy.y
        bullet_y1_height = self.bullet_y + self.bullet_height
        tankenemy_y2_width = tank_enemy.y + tank_enemy.width
        left_x = max(left_x1, left_x2)
        right_x = min(right_x1, right_x2)
        bullet_y_tankenemy_max = max(bullet_y1, tankenemy_y2)
        bullet_y_tankenemy_min = min(bullet_y1_height, tankenemy_y2_width)
        if left_x <= right_x and bullet_y_tankenemy_max <= bullet_y_tankenemy_min:
            return True
        return False


class Wall:

    def __init__(self, x_wall, y_wall):
        self.x_wall = x_wall
        self.y_wall = y_wall
        self.width_wall = 30
        self.height_wall = 15
        self.color = (3, 3, 3)

    def draw(self):
        pygame.draw.rect(screen, self.color,
                         (self.x_wall, self.y_wall, self.width_wall, self.height_wall))

    def collision_tank(self, tank_enemy):
        left_x1 = self.x_wall
        left_x2 = tank_enemy.x
        right_x1 = self.x_wall + self.width_wall
        right_x2 = tank_enemy.x + tank_enemy.width
        wall_y1 = self.y_wall
        ty2 = tank_enemy.y
        wall_height_y1 = self.y_wall + self.height_wall
        by2 = tank_enemy.y + tank_enemy.width
        left_x = max(left_x1, left_x2)
        right_x = min(right_x1, right_x2)
        wall_max_y = max(wall_y1, ty2)
        wall_min_y = min(wall_height_y1, by2)
        if left_x <= right_x and wall_max_y <= wall_min_y:
            return True
        return False

    def collision_bullet(self, bullet_enemy):
        left_x1 = self.x_wall
        left_x2 = bullet_enemy.bullet_x
        right_x1 = self.x_wall + self.width_wall
        right_x2 = bullet_enemy.bullet_x + bullet_enemy.bullet_width
        ty1 = self.y_wall
        ty2 = bullet_enemy.bullet_y
        by1 = self.y_wall + self.height_wall
        by2 = bullet_enemy.bullet_y + bullet_enemy.bullet_width
        lx = max(left_x1, left_x2)
        rx = min(right_x1, right_x2)
        ty = max(ty1, ty2)
        by = min(by1, by2)
        if lx <= rx and ty <= by:
            return True
        return False

class Fruit:

    def __init__(self, x_fruit, y_fruit):
        self.x_fruit = x_fruit
        self.y_fruit = y_fruit
        self.radius = 10
        self.color = (0, 255, 0)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x_fruit, self.y_fruit), self.radius)

    def collision_fruit(self, tank_enemy):
        left_x1 = self.x_fruit
        left_x2 = tank_enemy.x
        right_x1 = self.x_fruit + self.width_fruit
        right_x2 = tank_enemy.x + tank_enemy.width
        fruit_y1 = self.y_fruit
        tank_y2 = tank_enemy.y
        fruit_y1 = self.y_fruit + self.height_fruit
        tankenemy_y2 = tank_enemy.y + tank_enemy.width
        left_x = max(left_x1, left_x2)
        right_x = min(right_x1, right_x2)
        fruitTank_y = max(fruit_y1, tank_y2)
        fruitTankEnemy_y = min(fruit_y1, tankenemy_y2)
        if left_x <= right_x and fruitTank_y <= fruitTankEnemy_y:
            return True
        return False



game = True
sound_gg = False
tt = 0

tank0 = Tank(r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\up_green_tank.png', 60)
tank1 = Tank(r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\up_red_tank.png', 740,
             pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
# C:\games\Endterm\2Tank\mini_pictures_tank_sounds\tank1_up_red.png

tanks = [tank0, tank1]

bullet0 = Bullet(tank0)
bullet1 = Bullet(tank1, pygame.K_SPACE)

bullets = [bullet0, bullet1]

walls = []
for i in range(10):
    # x_wall = random.randint(0, 750)
    # y_wall = random.randint(0, 550)
    x_wall = random.randint(0, 750)
    y_wall = random.randint(0, 550)
    walls.append(Wall(x_wall, y_wall))

x_fruit = random.randint(0, 750)
y_fruit = random.randint(0, 550)
fruit = Fruit(x_fruit, y_fruit)

FPS = 30
clock = pygame.time.Clock()

a = 30


while game:
    mills = clock.tick(FPS)
    sec = mills / 1000
    a = a - sec
    print(a)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
            for tank in tanks:
                if event.key in tank.KEYS.keys():
                    move_sound.play()
                    tank.Change_dir(tank.KEYS[event.key])

            for bullet in bullets:

                if event.key in bullet.KEYS.keys():
                    bullet.direction_bullet()
                    bullet.bullet_pos()
                    if bullet.fire_yes == False:
                        fire.play()
                    bullet.fire_yes = True

    screen.fill((255, 255, 255))


    for bullet in bullets:
        bullet.move_bullet()

    if bullet0.collision_tank(tank1):
        explosion.play()
        if sound_gg == False:
            explosion.play()
        # tank1.random_pos()
        tank1.health_amount -= 1
        bullet0.bullet_x = -100
        bullet0.bullet_y = -100
        bullet0.fire_yes = False

    if bullet1.collision_tank(tank0):
        explosion.play()
        if sound_gg == False:
            explosion.play()
        # tank0.random_pos()
        tank0.health_amount -= 1
        bullet1.bullet_x = -100
        bullet1.bullet_y = -100
        bullet1.fire_yes = False

    for wall in walls:

        wall_stuk0 = False
        if wall.collision_tank(tank0):
            wall_stuk0 = True
            explosion.play()
            walls.remove(wall)
            tank0.health_amount -= 1
            break

        wall_stuk1 = False
        if wall.collision_tank(tank1):
            wall_stuk0 = True
            explosion.play()
            walls.remove(wall)
            tank1.health_amount -= 1
            break

        if wall.collision_bullet(bullet0):
            explosion.play()
            walls.remove(wall)
            break

        if wall.collision_bullet(bullet1):
            explosion.play()
            walls.remove(wall)
            break


    ###

    def GoodGame():
        for tank in tanks:
            tank.move()
            tank.health_of_tank()

            if tank.health_amount == 0:
                tank0.speed = 0
                tank1.speed = 0
                bullet0.bullet_speed = 0
                bullet1.bullet_speed = 0
                bullet0.fire_yes = True
                bullet1.fire_yes = True
                bullet0.bullet_x = 1100
                bullet1.bullet_x = 1100
                # mixer.music.stop()
                sound_gg = True
                # GoodGame_Sound()

                font = pygame.font.SysFont("Arial", 80)
                text = font.render("Game Over", 1, (0, 0, 0))
                place = text.get_rect(center=(400, 275))
                screen.blit(text, place)

                font = pygame.font.SysFont("Arial", 50)
                text = font.render("Press ESC to Exit", 1, (0, 0, 0))
                place = text.get_rect(center=(400, 335))
                screen.blit(text, place)

    # def GoodGame_Sound():
    #     Gameover_sound.play()

    screen.blit(bg, (0, 0))
    GoodGame()
    tank0.draw(), tank1.draw()
    tank0.health_of_tank(), tank1.health_of_tank()
    bullet0.draw_bullet(), bullet1.draw_bullet()


    for wall in walls:
        wall.draw()

    #
    # now = time.time()  # current time in seconds
    # if now - last_food > secs_until_food:
    #     # Create food object
    #     fruit = Fruit(x_fruit, y_fruit)
    #     fruit.draw()
    #     last_food = now
    #     secs_until_food = random.randint(10, 20)


    pygame.display.flip()



############################################# Multiplayer ######################################################

import json
from threading import Thread
import pika
import uuid
import sys
import pygame


IP = '34.254.177.17'
PORT = 5672
VIRTUAL_HOST = 'dar-tanks'
USERNAME = 'dar-tanks'
PASSWORD = '5orPLExUYnyVYZg48caMpX'
pygame.init()
screen = pygame.display.set_mode((1050, 600))
pygame.display.set_caption("Multiplayer Tank Game")
fire = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\fire_sound.wav')
move_sound = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\move_Sound.wav')
move_sound.set_volume(0.01)


class TankRpcClient:

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=IP,
                port=PORT,
                virtual_host=VIRTUAL_HOST,
                credentials=pika.PlainCredentials(
                    username=USERNAME,
                    password=PASSWORD
                )
            )
        )

        self.channel = self.connection.channel()
        queue = self.channel.queue_declare(queue='',
                                           auto_delete=True,
                                           exclusive=True
                                           )

        self.callback_queue = queue.method.queue
        self.channel.queue_bind(
            exchange='X:routing.topic',
            queue=self.callback_queue
        )

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response = None
        self.corr_id = None
        self.token = None
        self.tank_id = None
        self.room_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = json.loads(body)
            print(self.response)

    def call(self, key, message={}):
        self.response = None
        self.corr_id = str(uuid.uuid4())  # generate random fresh key
        self.channel.basic_publish(
            exchange='X:routing.topic',
            routing_key=key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(message)
        )

        while self.response is None:
            self.connection.process_data_events(time_limit=1)

    def check_server_status(self):
        self.call('tank.request.healthcheck')
        return self.response['status'] == '200'

    def obtain_token(self, room_id):
        message = {
            'roomId': room_id
        }
        self.call('tank.request.register', message)
        if 'token' in self.response:
            self.token = self.response['token']
            self.tank_id = self.response['tankId']
            self.room_id = self.response['roomId']
            return True
        return False

    def turn_tank(self, token, direction):
        message = {
            'token': token,
            'direction': direction
        }
        self.call('tank.request.turn', message)

    def fire_bullet(self, token):
        message = {
            'token': token
        }
        self.call('tank.request.fire', message)


class TankConsumerClient(Thread):

    def __init__(self, room_id):
        super().__init__()
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=IP,
                port=PORT,
                virtual_host=VIRTUAL_HOST,
                credentials=pika.PlainCredentials(
                    username=USERNAME,
                    password=PASSWORD
                )
            )
        )

        self.channel = self.connection.channel()
        queue = self.channel.queue_declare(queue='',
                                           auto_delete=True,
                                           exclusive=True
                                           )

        #####   Get messages from room   #####

        event_listener = queue.method.queue
        self.channel.queue_bind(exchange='X:routing.topic',
                                queue=event_listener,
                                routing_key='event.state.' + room_id)
        self.channel.basic_consume(
            queue=event_listener,
            on_message_callback=self.on_response,
            auto_ack=True
        )

        self.response = None

    def on_response(self, ch, method, props, body):
        self.response = json.loads(body)
        # print(self.response)

    def run(self):
        self.channel.start_consuming()


UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

MOVE_KEYS = {
    pygame.K_w: UP,
    pygame.K_s: DOWN,
    pygame.K_a: LEFT,
    pygame.K_d: RIGHT
}

is_fired = False


def draw_tank(id, x, y, width, height, direction, health, score, **kwargs):
    global tank_image, static_tank_image, enemy_image, static_tank_image
    tank_image = pygame.image.load(
        r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\tank1_up_yellow.png')
    static_tank_image = tank_image

    enemy_image = pygame.image.load(
        r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\tank2_up_red.png')
    static_enemy_image = enemy_image

    if id == client.tank_id:

        if direction == RIGHT:
            static_tank_image = pygame.transform.rotate(tank_image, -90)
        elif direction == LEFT:
            static_tank_image = pygame.transform.rotate(tank_image, 90)
        elif direction == UP:
            static_tank_image = pygame.transform.rotate(tank_image, 0)
        elif direction == DOWN:
            static_tank_image = pygame.transform.rotate(tank_image, 180)

### Here is writing od below, problem with blitting the picture is gone i move ###
        # font1 = pygame.font.Font('Arial', 10)
        # my_id = client.response['tankId']
        # text1 = font1.render('tankId: {}'.format(my_id), True, (255, 255, 255))
        # textRect1 = text1.get_rect()
        # textRect1.center = (x, y + 30)
        # # textRect = text.get_rect()
        # static_tank_image_rect = tank_image.get_rect()
        #
        # # static_tank_image.blit(text1, static_tank_image_rect)
        # static_tank_image_rect.blit(text1, (x - 15, y + 35))
        screen.blit(static_tank_image, (x, y))

    else:
        if direction == RIGHT:
            static_enemy_image = pygame.transform.rotate(enemy_image, -90)
        elif direction == LEFT:
            static_enemy_image = pygame.transform.rotate(enemy_image, 90)
        elif direction == UP:
            static_enemy_image = pygame.transform.rotate(enemy_image, 0)
        elif direction == DOWN:
            static_enemy_image = pygame.transform.rotate(enemy_image, 180)
        #  add id font
        screen.blit(static_enemy_image, (x, y))




def draw_bullet(x, y, direction, owner):

    if owner == client.tank_id:
        if direction == RIGHT:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, 15, 5))
        elif direction == LEFT:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, 15, 5))
        elif direction == UP:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, 5, 15))
        elif direction == DOWN:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, 5, 15))
    else:
        if direction == RIGHT:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 15, 5))
        elif direction == LEFT:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 15, 5))
        elif direction == UP:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 5, 15))
        elif direction == DOWN:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, 5, 15))


def draw_text(text_message, x, y, font_size, color):
    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(text_message, 1, color)
    place = text.get_rect(center=(x, y))
    screen.blit(text, place)


# def run_inf_panel():
#     ### health, score
#
#     return



def game_start():
    running = True
    font = pygame.font.Font('freesansbold.ttf', 17)

    while running:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (200, 200, 200), (800, 0, 1100, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # tank_image = pygame.image.load(
                #     r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\tank1_up_yellow.png')
                if event.key in MOVE_KEYS:
                    move_sound.play()
                    client.turn_tank(client.token, MOVE_KEYS[event.key])

                if event.key == pygame.K_SPACE:
                    fire.play()
                    client.fire_bullet(client.token)

        try:
            remaining_time = event_client.response['remainingTime']
            text = font.render('Remaining Time: {}'.format(
                remaining_time), True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (920, 550)
            screen.blit(text, textRect)
            draw_text("MY: ID        Health       Score", 900, 40, 15, (0, 0, 255))
            draw_text("Enemies     Health     Score", 900, 100, 15, (255, 0, 0))
            enemy_id_y = 0



            hits = event_client.response['hits']
            bullets = event_client.response['gameField']['bullets']
            winners = event_client.response['winners']
            losers = event_client.response['losers']
            kicked = event_client.response['kicked']
            hits = event_client.response['hits']
            tanks = event_client.response['gameField']['tanks']


            for tank in tanks:
                draw_tank(**tank)

            for tank in tanks:
                if client.tank_id == tank['id']:
                    draw_text(tank['id'] + "         " + str(tank['health']) + "                 " + str(tank['score']), 900,
                              70, 14, (0, 0, 255))
                else:
                    draw_text(tank['id'] + "            " + str(tank['health']) + "                 " + str(tank['score']), 895,
                              120 + (18 * enemy_id_y), 14, (255, 0, 0))
                    enemy_id_y += 1

            for bullet in bullets:
                # draw_bullet(**bullet)
                draw_bullet(bullet['x'], bullet['y'], bullet['direction'], bullet['owner'])

        except:
            pass
        pygame.display.flip()

    client.connection.close()
    pygame.quit()


client = TankRpcClient()
client.check_server_status()

client.obtain_token('room-17')
event_client = TankConsumerClient('room-17')
event_client.start()
game_start()
