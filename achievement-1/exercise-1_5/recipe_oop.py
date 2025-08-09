class Recipe:
    all_ingredients = set()
    
    def __init__(self, name, ingredients, cooking_time):
        """
        Initializes a Recipe object with name, ingredients, cooking time, and auto-generated difficulty.
        Ensures ingredients is a list of strings.
        """
        self.name = name
        # Ensure all items in ingredients are strings
        self.ingredients = [str(ing) for ing in ingredients]
        self.cooking_time = cooking_time
        self.difficulty = self.calc_difficulty(cooking_time, self.ingredients)
        self.update_all_ingredients()

    def __str__(self):
        # self.ingredients must be a list of strings for join() to work
        return (
            f"Name: {self.name}\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Cooking Time: {self.cooking_time}"
        )

    def __repr__(self):
        return f"Recipe(name={self.name}, ingredients={self.ingredients}, difficulty={self.difficulty})"
    
    def get_name(self):
        return self.name
    
    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()
    
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)
    
    def get_ingredients(self):
        return self.ingredients

    def calc_difficulty(self, cooking_time, ingredients):
        num_ingredients = len(ingredients)
        if cooking_time < 10 and num_ingredients < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and num_ingredients >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and num_ingredients < 4:
            difficulty = "Intermediate"
        elif cooking_time >= 10 and num_ingredients >= 4:
            difficulty = "Hard"
        return difficulty
    
    
    def get_difficulty(self):
        """
        Returns the difficulty. If not already calculated, calculates and stores it first.
        """
        if self.difficulty is None:
            self.difficulty = self.calc_difficulty(self.cooking_time, self.ingredients)
        return self.difficulty
    
    def search_ingredient(self, ingredient):
        """
        Searches for a specific ingredient in the recipe.
        """
        return ingredient in self.ingredients
    
    def get_cooking_time(self):
        return self.cooking_time

    def set_name(self, name):
        self.name = name
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

def recipe_search(data, search_term):
    print(f"\nRecipes containing '{search_term}':\n")
    for recipe in data:
        try:
            if recipe.search_ingredient(search_term):
                print(recipe)
                print("---")
        except Exception as e:
            print(f"Error searching in recipe {getattr(recipe, 'name', repr(recipe))}: {e}")

tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)

recipes = [tea, coffee, cake, smoothie]

print("\nRecipes list:")
print("-----------------------------------------")
for recipe in recipes:
    print(f"{recipe}\n---")

print("\nSearching for recipes by ingredient")
print("-----------------------------------------")
for search_term in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes, search_term)