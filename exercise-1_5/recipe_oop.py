class Recipe:
    all_ingredients = set()
    
    def __init__(self, name, ingredients, cooking_time):
        # Initialize the Recipe object with name, ingredients, cooking time, and difficulty
        self._name = name
        self._ingredients = ingredients
        self._cooking_time = cooking_time
        self._difficulty = None
        self.update_all_ingredients()  # Ensure all ingredients are tracked

    def __str__(self):
        return f"{self.name}: {self.ingredients} -> {self.instructions}"

    def __repr__(self):
        return f"Recipe(name={self.name}, ingredients={self.ingredients}, instructions={self.instructions})"