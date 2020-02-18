class Category:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items

    def __str__(self):
        output = f'{self.name} has: '
        for i in self.items:
            output += f'\n - {i}'
