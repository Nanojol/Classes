# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
class Storm:

    def __add__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __str__(self):
        return "Получили Шторм"


class Steam:

    def __add__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __str__(self):
        return "Получили Пар"


class Dirt:

    def __add__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __str__(self):
        return "Получили Грязь"


class Lightning:

    def __add__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __str__(self):
        return "Получили Молнию"


class Dust:

    def __add__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __str__(self):
        return "Получили Пыль"


class Lava:

    def __add__(self, part_1, part_2):
        self.part_1 = part_1
        self.part_2 = part_2

    def __str__(self):
        return "Получили Лаву"


# Storm
# Steam
# Dirt
# Lightning
# Dust
# Lava
class Water:
    def __str__(self):
        return "Я Вода"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None, "Ничего не вышло"


class Fire:
    def __str__(self):
        return "Я Огонь"

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None, "Ничего не вышло"


class Earth:
    def __str__(self):
        return "Я Земля"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Water):
            return Dirt()
        else:
            return None, "Ничего не вышло"


class Air:
    def __str__(self):
        return "Я Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None, "Ничего не вышло"


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

# print(Water(), '+', Air(), '=', Water() + Air())
water = Water()
air = Air()
earth = Earth()
fire = Fire()
result = water + air
print(water, air, result)
print(earth, fire, result)
