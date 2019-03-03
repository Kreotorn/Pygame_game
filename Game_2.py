import pygame
import math
import time

pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.mouse.set_visible(False)


class Pause:
    def __init__(self, sc):
        self.text_color = (250, 250, 250)
        self.lighter = False
        self.screen = sc

    def change_color(self):
        next_screen = pygame.Surface(self.screen.get_size())
        self.screen.fill(pygame.Color('Black'))

        font = pygame.font.Font(None, 100)
        text = font.render("Pause", 5, self.text_color)
        text_x = self.screen.get_width() // 2 - text.get_width() // 2
        text_y = self.screen.get_height() // 2 - text.get_height() // 2
        next_screen.blit(text, (text_x, text_y))

        self.screen.blit(next_screen, (0, 0))

        if 0 not in list(self.text_color):
            if 255 not in list(self.text_color):
                if self.lighter is False:
                    self.text_color = (self.text_color[0] - 5, self.text_color[1] - 5, self.text_color[2] - 5)
                else:
                    self.text_color = (self.text_color[0] + 5, self.text_color[1] + 5, self.text_color[2] + 5)
            else:
                self.lighter = False
                self.text_color = (self.text_color[0] - 5, self.text_color[1] - 5, self.text_color[2] - 5)
        else:
            self.lighter = True
            self.text_color = (self.text_color[0] + 5, self.text_color[1] + 5, self.text_color[2] + 5)


class Start:
    def __init__(self, sc):
        self.text_color = (250, 250, 250)
        self.lighter = False
        self.screen = sc

    def change_color(self):
        next_screen = pygame.Surface(self.screen.get_size())
        self.screen.fill(pygame.Color('Black'))

        font = pygame.font.Font(None, 100)
        text = font.render("Start", 5, self.text_color)
        text_x = self.screen.get_width() // 2 - text.get_width() // 2
        text_y = self.screen.get_height() // 2 - text.get_height() // 2
        next_screen.blit(text, (text_x, text_y))

        self.screen.blit(next_screen, (0, 0))

        if 0 not in list(self.text_color):
            if 255 not in list(self.text_color):
                if self.lighter is False:
                    self.text_color = (self.text_color[0] - 5, self.text_color[1] - 5, self.text_color[2] - 5)
                else:
                    self.text_color = (self.text_color[0] + 5, self.text_color[1] + 5, self.text_color[2] + 5)
            else:
                self.lighter = False
                self.text_color = (self.text_color[0] - 5, self.text_color[1] - 5, self.text_color[2] - 5)
        else:
            self.lighter = True
            self.text_color = (self.text_color[0] + 5, self.text_color[1] + 5, self.text_color[2] + 5)


class Game_over:
    def __init__(self, sc):
        self.text_color = (250, 250, 250)
        self.lighter = False
        self.screen = sc

    def change_color(self):
        next_screen = pygame.Surface(self.screen.get_size())
        self.screen.fill(pygame.Color('Black'))

        font = pygame.font.Font(None, 100)
        text = font.render("Game_over", 5, self.text_color)
        text_x = self.screen.get_width() // 2 - text.get_width() // 2
        text_y = self.screen.get_height() // 2 - text.get_height() // 2
        next_screen.blit(text, (text_x, text_y))

        self.screen.blit(next_screen, (0, 0))

        if 0 not in list(self.text_color):
            if 255 not in list(self.text_color):
                if self.lighter is False:
                    self.text_color = (self.text_color[0] - 5, self.text_color[1] - 5, self.text_color[2] - 5)
                else:
                    self.text_color = (self.text_color[0] + 5, self.text_color[1] + 5, self.text_color[2] + 5)
            else:
                self.lighter = False
                self.text_color = (self.text_color[0] - 5, self.text_color[1] - 5, self.text_color[2] - 5)
        else:
            self.lighter = True
            self.text_color = (self.text_color[0] + 5, self.text_color[1] + 5, self.text_color[2] + 5)


class Hero:
    def __init__(self, sc):
        self.position = (sc.get_width() // 2, sc.get_height() // 2)
        self.R = 20
        self.screen = sc
        self.hp = 200
        self.next_screen = pygame.Surface(self.screen.get_size())

    def move(self, way):
        if way == 'r':
            if self.position[0] != self.screen.get_width() - 20:
                self.position = (self.position[0] + 5, self.position[1])
        elif way == 'l':
            if self.position[0] != 20:
                self.position = (self.position[0] - 5, self.position[1])
        elif way == 'up':
            if self.position[1] != 20:
                self.position = (self.position[0], self.position[1] - 5)
        elif way == 'd':
            if self.position[1] != self.screen.get_height() - 20:
                self.position = (self.position[0], self.position[1] + 5)
        self.next_screen.fill(pygame.Color('Black'))
        pygame.draw.circle(self.next_screen, pygame.Color('Yellow'), self.position, self.R + 4)
        pygame.draw.circle(self.next_screen, pygame.Color('Black'), self.position, self.R + 3)
        pygame.draw.circle(self.next_screen, pygame.Color('Purple'), self.position, self.R)

    def f_move(self, way):
        for i in range(100):
            if way == 'r':
                if self.position[0] != self.screen.get_width() - 20:
                    self.position = (self.position[0] + 1, self.position[1])
                else:
                    break
            elif way == 'l':
                if self.position[0] != 20:
                    self.position = (self.position[0] - 1, self.position[1])
                else:
                    break
            elif way == 'up':
                if self.position[1] != 20:
                    self.position = (self.position[0], self.position[1] - 1)
                else:
                    break
            elif way == 'd':
                if self.position[1] != self.screen.get_height() - 20:
                    self.position = (self.position[0], self.position[1] + 1)
                else:
                    break

            pygame.draw.circle(self.next_screen, pygame.Color('Yellow'), self.position, self.R)

    def draw(self, bullets):
        no_damage = True
        pygame.draw.circle(self.next_screen, pygame.Color('Yellow'), self.position, self.R + 4)
        pygame.draw.circle(self.next_screen, pygame.Color('Black'), self.position, self.R + 3)
        pygame.draw.circle(self.screen, pygame.Color('Purple'), self.position, self.R)

        self.screen.blit(self.next_screen, (0, 0))

        for bullet in bullets:
            if (bullet[0][0] - self.position[0]) ** 2 + (bullet[0][1] - self.position[1]) ** 2 <= self.R ** 2:
                no_damage = False
                if self.hp > 0:
                    self.hp -= 5
                else:
                    return True
        if no_damage is False:
            self.next_screen.fill(pygame.Color('Red'))
            self.screen.blit(self.next_screen, (0, 0))

    def get_next_screen(self):
        return self.next_screen

    def get_position(self):
        return self.position

    def get_radius(self):
        return self.R

    def draw_HP(self):

        Rect = ((5, 3), (self.hp, 10))
        pygame.draw.rect(screen, (100, 200, 0), Rect, 0)

    def wave_damage(self, waves):
        for wave in waves:
            if wave[1] - self.R <= ((self.position[0] - wave[3][0]) ** 2
                                    + (self.position[1] - wave[3][1]) ** 2) ** 0.5 <= self.R + wave[1] + 3:
                self.hp -= 5
                self.next_screen.fill(pygame.Color('Green'))
                self.screen.blit(self.next_screen, (0, 0))


class Target:
    def __init__(self, center, next_screen):
        self.center = center
        self.screen = next_screen
        self.mouse_position = None
        self.ang = 30 / 180
        self.shots = []
        self.p1 = None
        self.last_shot = None

    def change_target(self, way):
        if way is True:
            dif = 0.06
        else:
            dif = - 0.06
        self.ang += dif

    def change_target_with_mouse(self, diff):
        self.ang -= diff / 150

    def target(self, hero_position):
        self.center = hero_position
        x = self.center[0]
        y = self.center[1]
        for i in range(2):
            p1 = (x + 50 * math.cos(self.ang * math.pi), y + 50 * math.sin(self.ang * math.pi))
            pygame.draw.circle(self.screen, pygame.Color('Yellow'), (int(p1[0]), int(p1[1])), 5)
            self.ang += 120 / 180

        self.p1 = (x + 50 * math.cos(self.ang * math.pi), y + 50 * math.sin(self.ang * math.pi))
        pygame.draw.circle(self.screen, pygame.Color('Red'), (int(self.p1[0]), int(self.p1[1])), 5)

        self.ang += 120 / 180

    def shot(self, hero_pos, enemy_pos, enemy_R):
        if self.last_shot is None:
            self.last_shot = time.time()
            try:
                tg = (self.p1[1] - hero_pos[1]) / (self.p1[0] - hero_pos[0])
            except ZeroDivisionError:
                tg = 0

            self.shots.append(((self.p1[0], self.p1[1]), (hero_pos[0], hero_pos[1]), tg, 8, 0))

        if time.time() - self.last_shot > 0.2:
            tg = (self.p1[1] - hero_pos[1]) / (self.p1[0] - hero_pos[0])

            if self.p1[1] - hero_pos[1] < 0 and self.p1[0] - hero_pos[0] < 0 or self.p1[0] - hero_pos[0] < 0:
                self.shots.append(((self.p1[0], self.p1[1]), (hero_pos[0], hero_pos[1]), tg, 8, -1))
            else:
                self.shots.append(((self.p1[0], self.p1[1]), (hero_pos[0], hero_pos[1]), tg, 8, 0))
            self.last_shot = time.time()
        shots = []

        for bullet in self.shots:

            if 0 <= bullet[0][0] <= self.screen.get_width() and 0 <= bullet[0][1] <= self.screen.get_height():
                try:
                    if bullet[4] < 0:
                        bullet = ((bullet[0][0] - (bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5,
                                   bullet[0][1] - (((bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5) * bullet[2])),
                                  bullet[1], bullet[2], bullet[3], -1)
                    else:
                        bullet = ((bullet[0][0] + (bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5,
                                   bullet[0][1] + ((bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5 * bullet[2])),
                                  bullet[1], bullet[2], bullet[3], 0)
                except ZeroDivisionError:
                    print('error')
                pygame.draw.circle(self.screen, pygame.Color('Red'), (int(bullet[0][0]), int(bullet[0][1])), 5)

                if (bullet[0][0] - enemy_pos[0]) ** 2 + (bullet[0][1] - enemy_pos[1]) ** 2 > (enemy_R // 2) ** 2:
                    shots.append(bullet)

        self.shots = shots

    def get_bullets(self):
        return self.shots


class Enemy:
    def __init__(self, sc):
        self.R = 20
        self.position = (200, 200)
        self.hp = 200
        self.screen = sc

        self.r_move = True
        self.up_move = True

        self.waves = []
        self.last_wave_time = 2

        self.teleport_pos = [(500, 500), (200, 80), (600, 100), (400, 300), (50, 50)]

        self.teleport_last = 4
        self.teleport_num = 0

        self.shots = []
        self.last_shot = None
        self.p1 = None

    def draw_enemy(self, bullets):
        no_damage = True

        for bullet in bullets:
            if (bullet[0][0] - self.position[0]) ** 2 + (bullet[0][1] - self.position[1]) ** 2 <= self.R ** 2:
                no_damage = False

        if no_damage is False:
            pygame.draw.circle(self.screen, pygame.Color('Red'), self.position, self.R)
            if self.hp != 0:
                self.hp -= 1
                return False
            else:
                return True

        else:
            pygame.draw.circle(self.screen, pygame.Color('Yellow'), self.position, self.R)
            return False

    def get_position(self):
        return self.position

    def get_radius(self):
        return self.R

    def get_bullets(self):
        return self.shots

    def set_position_in_danger(self):
        if self.r_move is True:
            if (self.screen.get_width() - self.position[0]) ** 2 > self.R ** 2 * 4:
                for i in range(40):
                    self.position = self.position[0] + 1, self.position[1]
                    pygame.draw.circle(self.screen, pygame.Color('Yellow'), self.position, self.R)
            else:
                self.r_move = False
        else:
            if (0 - self.position[0]) ** 2 > self.R ** 2 * 4:
                self.position = self.position[0] - 4, self.position[1]
                for i in range(40):
                    self.position = self.position[0] - 1, self.position[1]
                    pygame.draw.circle(self.screen, pygame.Color('Yellow'), self.position, self.R)
            else:
                self.r_move = True

        if self.up_move is True:
            if (self.screen.get_height() - self.position[1]) ** 2 > self.R ** 2 * 4:
                for i in range(20):
                    self.position = self.position[0], self.position[1] + 2
                    pygame.draw.circle(self.screen, pygame.Color('Yellow'), self.position, self.R)
            else:
                self.up_move = False
        else:
            if (0 - self.position[1]) ** 2 > self.R ** 2 * 4:
                for i in range(20):
                    self.position = self.position[0], self.position[1] - 2
                    pygame.draw.circle(self.screen, pygame.Color('Yellow'), self.position, self.R)
            else:
                self.up_move = True

    def wave(self):
        if time.time() - self.last_wave_time >= 1.5:
            self.waves.append((self.position, 20, time.time(), self.position))
            self.last_wave_time = time.time()

        waves = []
        for wave in self.waves:
            if wave[1] <= 200:
                if time.time() - wave[2] > 0.001:
                    pygame.draw.circle(self.screen, pygame.Color('Red'), wave[0], wave[1])
                    pygame.draw.circle(self.screen, pygame.Color('Black'), wave[0], wave[1] - 5)
                waves.append((wave[0], wave[1] + 3, time.time(), wave[3]))

        self.waves = waves

    def get_wave(self):
        return self.waves

    def teleportate(self):
        if time.time() - self.teleport_last >= 3:
            self.teleport_last = time.time()
            if self.teleport_num != len(self.teleport_pos) - 1:
                self.teleport_num += 1
            else:
                self.teleport_num = 0
            self.position = self.teleport_pos[self.teleport_num]

    def shot(self, hero_pos, hero_R):
        self.p1 = self.position
        if self.last_shot is None:
            self.last_shot = time.time()
            try:
                tg = (self.p1[1] - hero_pos[1]) / (self.p1[0] - hero_pos[0])
            except ZeroDivisionError:
                tg = 0

            self.shots.append(((self.p1[0], self.p1[1]), (hero_pos[0], hero_pos[1]), tg, 8, 0))

        if time.time() - self.last_shot > 0.4:
            try:
                tg = (self.p1[1] - hero_pos[1]) / (self.p1[0] - hero_pos[0])
            except ZeroDivisionError:
                tg = 0
            if self.p1[1] - hero_pos[1] > 0 and self.p1[0] - hero_pos[0] > 0 or self.p1[0] - hero_pos[0] > 0:
                self.shots.append(((self.p1[0], self.p1[1]), (hero_pos[0], hero_pos[1]), tg, 8, -1))
            else:
                self.shots.append(((self.p1[0], self.p1[1]), (hero_pos[0], hero_pos[1]), tg, 8, 0))
            self.last_shot = time.time()
        shots = []

        for bullet in self.shots:

            if 0 <= bullet[0][0] <= self.screen.get_width() and 0 <= bullet[0][1] <= self.screen.get_height():
                try:
                    if bullet[4] < 0:
                        bullet = ((bullet[0][0] - (bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5,
                                   bullet[0][1] - (((bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5) * bullet[2])),
                                  bullet[1], bullet[2], bullet[3], -1)
                    else:
                        bullet = ((bullet[0][0] + (bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5,
                                   bullet[0][1] + ((bullet[3] ** 2 / (1 + bullet[2] ** 2)) ** 0.5 * bullet[2])),
                                  bullet[1], bullet[2], bullet[3], 0)
                except ZeroDivisionError:
                    print('error')
                pygame.draw.circle(self.screen, pygame.Color('White'), (int(bullet[0][0]), int(bullet[0][1])), 5)
                if (bullet[0][0] - hero_pos[0]) ** 2 + (bullet[0][1] - hero_pos[1]) ** 2 > (hero_R // 2) ** 2:
                    shots.append(bullet)

        self.shots = shots

    def draw_HP(self):

        Rect = ((self.screen.get_width() - 210, 3), (self.hp, 10))
        pygame.draw.rect(screen, (255, 30, 0), Rect, 0)


'''Game'''

run_game = True

hero = Hero(screen)
start = Start(screen)
game_over = Game_over(screen)
enemy = Enemy(hero.get_next_screen())
pause = Pause(screen)

target = Target(hero.get_position(), hero.get_next_screen())
way = None
started = False
death = False
shot = False
last_pos = None
distation = 300
stop = False
diff = 0
last_x = 200
use_mouse = False

fps = pygame.time.Clock()
fps_num = 60

pygame.mixer.music.load('OST.mp3')
pygame.mixer.music.play(-1)

while run_game is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.KEYDOWN:

            started = True

            if event.key == pygame.K_a:
                hero.move('l')
                way = 'l'
            elif event.key == pygame.K_e:
                shot = True
            elif event.key == pygame.K_d:
                hero.move('r')
                way = 'r'
            elif event.key == pygame.K_w:
                hero.move('up')
                way = 'up'
            elif event.key == pygame.K_s:
                hero.move('d')
                way = 'd'
            elif event.key == pygame.K_SPACE and way is not None:
                way += 'f'
            elif event.key == pygame.K_4:
                if stop is True:
                    stop = False
                    pygame.mixer.music.set_volume(1)
                else:
                    stop = True
                    pygame.mixer.music.set_volume(0.3)
            elif event.key == pygame.K_1:
                if use_mouse is False:
                    use_mouse = True
                else:
                    use_mouse = False
        if event.type == pygame.KEYUP:
            button = None
            if way == 'l':
                button = pygame.K_a
            elif way == 'r':
                button = pygame.K_d
            elif way == 'up':
                button = pygame.K_w
            elif way == 'd':
                button = pygame.K_s
            elif way is not None:
                if 'f' in way:
                    button = pygame.K_d

            if event.key == button and button is not None:
                way = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                if use_mouse is False:
                    target.change_target(True)
            elif event.button == 4:
                if use_mouse is False:
                    target.change_target(False)
        if event.type == pygame.MOUSEMOTION:
            if use_mouse is True:
                diff = last_x - pygame.mouse.get_pos()[0]
                last_x = pygame.mouse.get_pos()[0]
                target.change_target_with_mouse(diff)

    if started is False:
        start.change_color()
        fps_num = 30
    elif death is True:
        game_over.change_color()
    elif stop is True:
        pause.change_color()
    else:
        fps_num = 60
        if way == 'l':
            hero.move('l')
        elif way == 'r':
            hero.move('r')
        elif way == 'up':
            hero.move('up')
        elif way == 'd':
            hero.move('d')
        elif way is not None and 'f' in way:
            hero.f_move(way[0: -1])
            way = way[0: -1]

        if last_pos != hero.get_position():
            last_pos = hero.get_position()
        else:
            hero.get_next_screen().fill(pygame.Color('Black'))
        enemy.wave()
        target.target(hero.get_position())
        target.shot(hero.get_position(), enemy.get_position(), enemy.get_radius())

        if (enemy.get_position()[0] - hero.get_position()[0]) ** 2 + (enemy.get_position()[1] -
                                                                      hero.get_position()[1]) ** 2 <= distation ** 2:
            enemy.set_position_in_danger()

        enemy.teleportate()
        hero.wave_damage(enemy.get_wave())

        if enemy.draw_enemy(target.get_bullets()) is True:
            death = True
        enemy.shot(hero.get_position(), hero.get_radius())
        if hero.draw(enemy.get_bullets()) is True:
            death = True
        enemy.draw_HP()
        hero.draw_HP()

    fps.tick(fps_num)
    pygame.display.flip()