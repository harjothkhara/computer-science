class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"\nYou have picked up: {self.name}\n")

    def on_drop(self):
        print(f"\nYou have dropped: {self.name}\n")

    def __str__(self):
        return f'Item List(name: {self.name}, description: {self.description}'

    def __repr__(self):
        """
      REPR method for the Room class
      """
        return f"Item({repr(self.name)})"


# i = Item("gun", "good looking gun")
# print(i)
