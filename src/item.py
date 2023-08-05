import csv
import math

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
            return self.__name
        self.__name = name
        return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='', encoding='windows-1251') as f:
            reader = csv.reader(f)
            for row in reader:
                name, price, quantity = row
                if price.isalpha():
                    continue
                emp = cls(name, price, quantity)
                cls.all.append(emp)

    @staticmethod
    def string_to_number(str_num):
        return math.floor(float(str_num))


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
