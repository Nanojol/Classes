# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (1800, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.count_fallen = 0
        self.all_random_values = []
        self.colour = sd.COLOR_WHITE

    def create_snow(self, center_x, center_y, length, colour, factor_a, factor_b, factor_c):
        dict_user = {
            'center_x': center_x,
            'center_y': center_y,
            'length': length,
            'colour': colour,
            'factor_a': factor_a,
            'factor_b': factor_b,
            'factor_c': factor_c,
        }
        self.all_random_values.append(dict_user)
        for i in self.all_random_values:
            point = sd.get_point(i['center_x'], i['center_y'])
            sd.snowflake(point, i['length'], i['colour'], i['factor_a'], i['factor_b'], i['factor_c'])

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):

        for i in self.all_random_values:
            point_starter = sd.get_point(i['center_x'], i['center_y'])
            sd.snowflake(point_starter, i['length'], sd.background_color, i['factor_a'], i['factor_b'], i['factor_c'])
            i['center_y'] -= 10
            i['center_x'] -= sd.randint(-10, 10)

    def draw(self):
        for i in self.all_random_values:
            point_starter = sd.get_point(i['center_x'], i['center_y'])
            sd.snowflake(point_starter, i['length'], self.colour, i['factor_a'], i['factor_b'], i['factor_c'])

    def can_fall(self):
        for i in self.all_random_values:
            center_y = i['center_y']
            if center_y > 0:
                return True
            else:
                return False

    def get_fallen_flakes(self):

        for i in self.all_random_values:
            if i['center_y'] < 1:
                self.count_fallen += 1
                self.all_random_values.remove(i)
        return self.count_fallen

    def append_flakes(self, count):

        for _ in range(count):
            self.all_random_values.append(self.random_values_snow())


    def random_values_snow(self):
        return {

            'center_x': random.randrange(50, 1600),
            'center_y': random.randrange(500, 650, 50),
            'factor_a': random.randrange(1, 8) / 10,
            'factor_b': random.randrange(1, 8) / 10,
            'factor_c': random.randrange(30, 60),
            'length': random.randrange(20, 50),

        }

    def get_flakes(self, count):

        for _ in range(count):
            self.all_random_values.append(self.random_values_snow())

        return self.all_random_values


flake = Snowflake()
# ВАРИАНТ 1
# flake.create_snow(center_x=50, center_y=550, length=40, colour=(255, 255, 255), factor_a=.7, factor_b=.5,
#                   factor_c=.3)
#
# #
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = flake.get_flakes(count=2)  # создать список снежинок

while True:
    for i in flakes:
        # flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = flake.get_fallen_flakes()  # подcчитать сколько снежинок уже упало
    print(fallen_flakes)
    if not flake.can_fall():
        flake.append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
