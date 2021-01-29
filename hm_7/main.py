#Задание 1

class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        self.max = len(self.matrix_list)

    def __iter__(self):
        self.i = 0
        while self.i < self.max:
            yield self.matrix_list[self.i]
            self.i += 1

    def __add__(self, other):
        return Matrix([[k + m for k, m in zip(l, n)] for l, n in zip(self.matrix_list, other.matrix_list)])

    def __str__(self):
        result = ''
        for row in self.matrix_list:
            result += ' '.join(list(map(str, row)))
            result += '\n'
        return result


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
c = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])

print(a)
print(a + b)
print(a + b + c)



# Задание 2

class Clothing:

    def __init__(self, name):
        self.name = name

class Coat(Clothing):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def cloth_consumption(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'Пальто: {self.name}, размер: {self.size}, расход ткани: {self.cloth_consumption}'


class Costume(Clothing):

    def __init__(self, name, growth):
        super().__init__(name)
        self.growth = growth

    @property
    def cloth_consumption(self):
        return 2 * self.growth + 0.3

    def __str__(self):
        return f'Костюм: {self.name}, рост: {self.growth}, расход ткани: {self.cloth_consumption}'


coat = Coat('burberry', 42)
print(coat)

costume = Costume('hugo boss', 182)
print(costume)



# Задание 3

class Cell:

    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus > other.nucleus:
            return Cell(self.nucleus - other.nucleus)
        else:
            return 'Результат должен быть больше нуля'

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def __str__(self):
        return f'Количество ячеек: {self.nucleus}'

    def make_order(self, nucleus_row):
        output = ''
        result = [['*' * nucleus_row] for j in range(self.nucleus // nucleus_row)]

        for element in result:
            output += ''.join(element)
            output += '\n'

        if self.nucleus % nucleus_row == 0:
            return output[:len(output) - 1]
        else:
            output += '*' * (self.nucleus % nucleus_row)
            return output


cell1 = Cell(12)
cell2 = Cell(9)

print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)
print(cell1.make_order(6))
print('-------------------')
print(cell2.make_order(5))
print('-------------------')
print((cell1+cell2).make_order(5))