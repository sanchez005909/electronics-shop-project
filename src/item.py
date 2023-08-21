import csv
import math
from src.config import path
import os.path

class InstantiateCSVError(Exception):

    def __init__(self, *args, **kwargs):
        self.message = f'Файл {path} поврежден'


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
        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.name}\', {round(self.price)}, {self.quantity})'

    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        try:

            Item.all.clear()
            with open(path, newline='', encoding='windows-1251') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if len(row) != 3:
                        raise InstantiateCSVError
                    name = row['name']
                    price = row['price']
                    quantity = row['quantity']
                    cls(name, price, quantity)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')

        except InstantiateCSVError as ex:
            print(ex.message)


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

    def __add__(self, other):
        if isinstance(other, (Item)):
            return self.quantity + other.quantity