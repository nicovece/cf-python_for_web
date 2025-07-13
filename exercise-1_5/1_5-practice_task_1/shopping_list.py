class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def __str__(self):
        return f"{self.list_name}:\n{self.shopping_list}"
    
    def __repr__(self):
        return f"ShoppingList(name={self.list_name}, items={self.shopping_list})"
    
    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append(item)
            print(f"{item} has been added to the shopping list\n---")
        else:
            print(f"{item} is already in the shopping list\n---")

    def remove_item(self, item):
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list\n---")
        else:
            print(f"{item} is not in the shopping list\n---")

    def view_list(self):
        print(self.shopping_list)

    def populate_from_input(self):
        print("\nEnter items for your shopping list. Type 'done' when finished.\n")
        while True:
            item = input("Enter the item (or 'done' to finish): ")
            if not item.strip():
                print("---\nYou must enter an item name (or 'done' to finish).\n---")
                continue
            if item.lower() == 'done':
                break
            self.add_item(item)

    def remove_item_from_input(self):
        print("\nEnter items to remove from your shopping list. Type 'done' when finished.\n")
        while True:
            item = input("Enter the item (or 'done' to finish): ")
            if not item.strip():
                print("---\nYou must enter an item name (or 'done' to finish).\n---")
                continue
            if item.lower() == 'done':
                break
            if item in self.shopping_list:
                self.remove_item(item)
            else:
                print(f"{item} is not in the shopping list. Try again.\n---")

# Create a shopping list instance
pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.populate_from_input()
print(f"---\n\n{pet_store_list}\n\n---")

pet_store_list.remove_item_from_input()
print("Removing items from the shopping list...")
print(f"---\n\n{pet_store_list}\n\n---")

