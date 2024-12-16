class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        with open(self.__file_name, 'a') as file:
            pass

    def get_products(self) -> str:
        """Считывает все товары из файла и возвращает их строкой."""
        try:
            with open(self.__file_name, 'r') as file:
                products = file.readlines()
                return ''.join(products).strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        """Добавляет товары в файл, если их ещё нет."""
        existing_products = self.get_products()
        existing_names = {line.split(', ')[0] for line in existing_products.split('\n') if line.strip()}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_names:
                    print(f"Продукт {product.name} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')
                    print(f"Продукт {product.name} добавлен в магазин")

if __name__ == "__main__":

    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')


    print(p2)
    s1.add(p1, p2, p3)
    print(s1.get_products())
