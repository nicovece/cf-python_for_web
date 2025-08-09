import pickle

recipes = []

while True:
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma separated): ").split(',')
    cooking_time = input("Enter the cooking time: ")
    difficulty = input("Enter the difficulty: ")

    recipe = {
        'name': name,
        'ingredients': [ingredient.strip() for ingredient in ingredients],
        'cooking_time': cooking_time,
        'difficulty': difficulty
    }
    recipes.append(recipe)
    
    another = input("Add another recipe? (y/n): ")
    if another.lower() != 'y':
        break

with open('exercise-1_4/1_4-practice_task_2/recipes.bin', 'wb') as file:
    pickle.dump(recipes, file)

with open('exercise-1_4/1_4-practice_task_2/recipes.bin', 'rb') as file:
    loaded_recipes = pickle.load(file)

for recipe in loaded_recipes:
    print("Recipe details - ")
    print("Name:  " + recipe['name'])
    print("Ingredients: " + str(recipe['ingredients']))
    print("Cooking time: " + recipe['cooking_time'])
    print("Difficulty: " + recipe['difficulty'])