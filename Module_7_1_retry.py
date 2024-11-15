class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = []

        # Считываем существующие продукты из файла, если он есть
        try:
            with open(self.__file_name, 'r') as file:
                existing_products = [line.split(', ')[0] for line in file]
        except FileNotFoundError:
            pass  # Файл не существует

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + 'n')
                print(f'Продукт {product} добавлен в магазин')


# Пример работы программы
s1 = Shop()
p1 = Product('Картошка', 50.5, 'Овощи')
p2 = Product('Спагетти', 3.4, 'Продукты')
p3 = Product('Картошка', 5.5, 'Овощи')

print(p2)  # выводим информацию о продукте

s1.add(p1, p2, p3)

print(s1.get_products())
