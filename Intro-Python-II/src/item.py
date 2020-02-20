class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You have picked up: {self.name}")

    def _on_drop(self):
        print(f"You have dropped: {self.name} ")

    def __str__(self):
        return f'Item(name: {self.name}, description: {self.description}'

    def __repr__(self):
        """
      REPR method for the Room class
      """
        return f"Item({repr(self.name)})"


# i = Item("gun", "good looking gun")
# print(i)
