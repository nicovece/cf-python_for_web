recipes_list = []
ingredients_list = []
while True:
    try:
        n = int(input("Enter the number of recipes: "))
        break
    except ValueError:
        print("Please enter a valid integer for the number of recipes.")

def take_recipe(i):
    print(f"\nRecipe {i+1}:")
    name = input("Enter recipe name: ")
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("Please enter a valid integer for the cooking time.")
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients (comma separated): ").split(",")]
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

for i in range(n):
    recipe = take_recipe(i)
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

print(f"\n\nRecipes list:\n------------------------------")
for recipe in recipes_list:
    # Calculate difficulty as per the rules
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and num_ingredients >= 4:
        difficulty = "Hard"
    print("\n")
    print(f"Recipe: {recipe['name']}")
    print(f"Cooking time: {cooking_time} minutes")
    print(f"Difficulty: {difficulty}")
    print(f"Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")

print(f"\n\nIngredients available across all recipes\n------------------------------\n")
ingredients_list.sort()
for ingredient in ingredients_list:
    print(f"- {ingredient}")