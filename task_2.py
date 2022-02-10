class Lemonade:
    def __init__(self, additive):
        if isinstance(additive, str):
            self.additive = additive
        else:
            self.ingredient = None

    def drink_info(self):
        if self.additive:
            print(f'Газировка и {self.additive}')
        else:
            print('Обычная газировка')