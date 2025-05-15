#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self._transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        self._transactions.append((title, price, quantity))

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100.0)
            self.total -= discount_amount
            
            formatted_total = f"{self.total:.2f}"
            if formatted_total.endswith('.00'):
                formatted_total = formatted_total[:-3]
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self._transactions:
            last_item_name, last_item_price, last_item_quantity = self._transactions.pop()
            self.total -= last_item_price * last_item_quantity