class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read().strip()

    def add(self, *products):
        existing_names = set()

        try:
            with open(self.__file_name, 'r+') as file:
                for line in file:
                    product_data = line.strip().split(', ')
                    existing_names.add(product_data[0])

                for product in products:
                    if product.name not in existing_names:
                        file.write(f"\n{product}")
                        existing_names.add(product.name)
                    else:
                        print(f"Продукт {product} уже есть в магазине")
        except FileNotFoundError:
            with open(self.__file_name, 'w') as file:
                for product in products:
                    file.write(f"{product}\n")



# Создаем объекты классов
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Проверяем метод __str__ для одного из продуктов
print(p2)

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Считываем все продукты из файла
print(s1.get_products())