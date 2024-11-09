from pprint import pprint

class Product:   # Создание класса
    def __init__(self, name, weight, category):   # Создаем конструктор
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):      #
        return f'{self.name} - ({self.weight} , {self.category})'


class Shop(Product):     # Создаем класс магазина
    def __init__(self, name, weight, category, __filename='product.txt'):
        super().__init__(name, weight, category)
        self.__filename = __filename

    def get_products(self):
        file = open(self.__filename, 'r')
        ac = file.read()
        file.close()
        print(f'{ac}')

    def add(self, *products):
        for i in products:
            s = (str(i))
            file = open(self.__filename, 'r')
            f = file.read()
            file.close()
            if s in f:
                print(f'Продукт {s} уже есть в магазине')
            else:
                file = open(self.__filename, 'a')
                file.write(f'\n{s}')
                file.close()


s1 = Shop('Dead rat', 0.1 , 'Цфыеу')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
