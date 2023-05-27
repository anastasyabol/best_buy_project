from abc import ABC, abstractmethod

class Promotion(ABC):
    """abstract class, apply promotion changes behavior of buy method in product, differently for each promotion"""
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    """Promotion calculates every second item half priced"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def apply_promotion(self, product, quantity):
        discount_price = product.price * quantity / 2 * 1.5
        if quantity % 2 == 0:
            return discount_price
        else:
            return discount_price + product.price


class ThirdOneFree(Promotion):
    """Promotion calculates every third item as free"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def apply_promotion(self, product, quantity):
        if quantity % 3 == 0:
            return product.price * quantity / 3 * 2
        else:
            return (product.price * quantity / 3 * 2) + (quantity % 3 * product.price)


class PercentDiscount():
    """Promotion calculates discount, percent is variable"""
    def __init__(self, name, percent):
        self.name = name
        self.percent = (100 - percent) / 100

    def __repr__(self):
        return f'{self.name}'

    def apply_promotion(self, product, quantity):
        return product.price * quantity * self.percent
