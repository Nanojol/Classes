class Bread:

    def __str__(self):
        return 'Я хлеб'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sausage:

    def __str__(self):
        return 'Я колбаса'

    def __add__(self, other):
        return Sandwich(part1=self, part2=other)


class Sandwich:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Я бутерброд. Состою из ' + str(self.part1) + ' и ' + str(self.part2)


borodinsky = Bread()
salami = Sausage()
result = borodinsky + salami
print(borodinsky,salami,result)