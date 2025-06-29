recipes_list = []
ingredients_list = []
while True:
    try:
        n = int(input("Enter the number of recipes: "))
        break
    except ValueError:
        print("Please enter a valid integer for the number of recipes.")

def take_recipe():
    print(f"\nRecipe {i+1}:")
    name = input("Enter recipe name: ")
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("Please enter a valid integer for the cooking time.")
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients (comma separated): ").split(",")]
    difficulty = ""
    print("\n--------------------------------")
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }
    for ingredient in ingredients:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for i in range(n):
    take_recipe()

print(f"\n\nRecipes list:\n------------------------------")
for recipe in recipes_list:
    print("\n")
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking time: {recipe['cooking_time']} minutes")
    print(f"Difficulty: {recipe['difficulty']}")
    print(f"Ingredients: {recipe['ingredients']}")

print(f"\n\nIngredients available across all recipes\n------------------------------\n")
for ingredient in ingredients_list:
    print(f"- {ingredient}")