"""Здесь надо написать тесты с использованием pytest для модуля item."""
"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)

    # Testing#1 test_calculate_total_price
assert item1.calculate_total_price() == item1.price * item1.quantity

    # Testing#2 test_apply_discount
assert item1.apply_discount() == None