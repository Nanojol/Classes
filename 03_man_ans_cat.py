# -*- coding: utf-8 -*-


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.cash = 100
        self.weakness = 0
        self.homeless = True
        self.home = None
        self.cat = None


    def __str__(self):
        return 'Я - {}, голод {}, усталость {}, Собственные деньги {}'.format(
            self.name, self.hunger, self.weakness,self.cash)

    def go_to_work(self):
        self.cash += 50
        self.hunger += 30
        self.weakness += 20
        print("Сходил на работу")

    def play_with_cat(self):
        self.cat.cat_weakness += 50
        self.weakness -= 30
        self.hunger += 10
        print("Поиграл с котом")

    def check_in_home(self, home):
        self.home = home
        self.hunger += 20
        self.cash -= 90
        self.homeless = False
        print("Заселился")

    def go_to_shop(self):
        if self.cash > 9:

            self.home.food += 50
            self.weakness += 10
            print("Купил еды")
            if self.home.cat_food < 100:
                self.home.cat_food += 40
                self.cash -= 60
            else:
                self.cash -= 40
        else:
            print("!!!!!!!! Деньги Кончились !!!!!!!!")
            if self.home.cash > 9:
                print("Достал деньги из заначки, иду в магазин")
                self.home.cash -= 40
                self.home.food += 50
                self.weakness += 10
            else:
                print("!!!!!!!! Деньги Кончились ВЕЗДЕ !!!!!!!!")

    def find_cat(self, cat):
        self.cat = cat
        self.cat.cat_home = self.home
        print("Нашёл кошку")

    def eating(self):
        self.hunger -= 50
        self.home.food -= 20
        print("Поел")

    def act(self):
        self.go_to_work()
        if self.cash > 100:
            self.cash -= 90
            self.home.cash += 90

        if self.hunger > 20 and self.home.food > 20:
            self.eating()
        elif self.cash < 10:
            self.go_to_work()
        elif self.weakness > 70:
            self.play_with_cat()
        elif self.home.cat_food < 30 or self.home.food < 50:
            self.go_to_shop()

        if self.home.dirty > 60:
            self.clean()
        self.home.dirty += 10
        self.sleep()

    def clean(self):
        self.home.dirty = 0
        self.weakness = 80
        print("Убрался")

    def sleep(self):
        self.weakness -= 30
        if self.weakness < 0:
            self.weakness = 0
        print("Поспал")


class House:

    def __init__(self):
        self.food = 0
        self.cat_food = 0
        self.cash = 0
        self.dirty = 0

    def __str__(self):
        if self.dirty > 50:
            return 'В Доме Грязно!!! В доме человеческой еды осталось {}, кошачей осталось {}. Денег в доме = {}'.format(
                self.food, self.cat_food, self.cash)
        else:
            return 'В Доме Чисто!!! В доме человеческой еды осталось {}, кошачей осталось {}. Денег в доме = {}'.format(
                self.food, self.cat_food, self.cash)


class Cat:

    def __init__(self, name):
        self.cat_name = name
        self.cat_hunger = 0
        self.cat_weakness = 0
        self.cat_home = None

    def __str__(self):
        return 'Я - {}, голод {}, усталость {}'.format(
            self.cat_name, self.cat_hunger, self.cat_weakness)

    def cat_act(self):
        self.cat_play()
        if self.cat_hunger > 60 and self.cat_weakness < 70:
            self.cat_eating()
        elif self.cat_weakness > 70:
            self.cat_go_to_sleep()

    def cat_eating(self):
        self.cat_hunger -= 50
        self.cat_home.food -= 20
        print("Cat Поел")

    def cat_go_to_sleep(self):
        self.cat_weakness -= 80
        if self.cat_weakness < 0:
            self.cat_weakness = 0
        print("Cat Поспал")

    def cat_play(self):
        self.cat_weakness += 30
        self.cat_hunger += 20
        print("Cat Поиграл")


my_sweet_home = House()
John = Man(name="John")
Marci = Cat(name="Marci")
John.check_in_home(my_sweet_home)
John.find_cat(cat=Marci)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    John.act()
    Marci.cat_act()
    print('--- в конце дня ---')
    print(John, Marci)
    print(my_sweet_home)


