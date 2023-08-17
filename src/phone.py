from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count):
        if count > 0 and isinstance(count, int):
            self.__number_of_sim = count
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')


    def __repr__(self):
        return f'{self.__class__.__name__}(\'{self.name}\', {round(self.price)}, {self.quantity}, {self.number_of_sim})'
