"""Здесь надо написать тесты с использованием pytest для модуля item."""
"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert item1.calculate_total_price() == item1.price * item1.quantity

def test_apply_discount():
    assert item1.apply_discount() == None
    assert item1.price == 10000

def test_name():
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5

def test_string_to_number():
    assert Item.string_to_number('7.9') == 7
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test__repr__():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__():
    assert str(item1) == 'Смартфон'

def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10