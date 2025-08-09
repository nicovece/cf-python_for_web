import pickle
import os

recipes_list = []
ingredients_list = []
while True:
    try:
        n = int(input("\nEnter the number of recipes: "))
        break
    except ValueError:
        print("\nPlease enter a valid integer for the number of recipes.")

def take_recipe(i):
    print(f"\nRecipe {i+1}:")
    name = input("Enter recipe name: ")
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("\nPlease enter a valid integer for the cooking time.")
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients (comma separated): ").split(",")]
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }
    return recipe

def calc_difficulty(cooking_time, ingredients):
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

for i in range(n):
    recipe = take_recipe(i)
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

# After collecting recipes, update the data dictionary with the new lists
# This ensures the latest recipes and ingredients are saved
# This step is important even if the file was loaded, so we always save the latest data

data = {
    'recipes_list': recipes_list,
    'all_ingredients': ingredients_list
}

script_dir = os.path.dirname(__file__)
filename = input("\n---\n\nEnter the filename where you've stored your recipes: ")
if not filename.endswith('.bin'):
    filename += '.bin'
filepath = os.path.join(script_dir, filename)

# Try to load existing data from the file, or create new data if not found/corrupted
try:
    file = open(filepath, 'rb')
    # Attempt to load the data dictionary from the file using pickle
    # We expect the file to contain a dictionary with two keys:
    #   'recipes_list' and 'all_ingredients'
    data = pickle.load(file)
    print("\n---\nData loaded successfully from file.")
except FileNotFoundError:
    # This block runs if the file does not exist
    print(f"---\nFile not found. A new data dictionary will be created and saved as '{filename}'.")
    # Create a new data dictionary with the current recipes and ingredients
    data = {
        'recipes_list': recipes_list,
        'all_ingredients': ingredients_list
    }
except Exception as error:
    # This block runs for any other exception (e.g., file is corrupted)
    print(f"---\nAn error occurred while loading the file: {error}")
    print("---\nCreating new data dictionary.")
    data = {
        'recipes_list': recipes_list,
        'all_ingredients': ingredients_list
    }
else:
    file.close()  # Always close the file when done reading
    print("---\nFile closed after usage.")
finally:
    # This block always runs, no matter what happened above
    # Extract the lists from the data dictionary
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']
    print("---\nData is ready for use!")
    # Save the updated data dictionary to the file
    # This ensures that any new recipes/ingredients are persisted
    with open(filepath, 'wb') as file:
        pickle.dump(data, file)
    print("---\nData saved successfully!")

# print(f"\n\nRecipes list:\n------------------------------")
# for recipe in recipes_list:
#     print("\n")
#     print(f"Recipe: {recipe['name']}")
#     print(f"Cooking time: {recipe['cooking_time']} minutes")
#     print(f"Difficulty: {recipe['difficulty']}")
#     print(f"Ingredients:")
#     for ingredient in recipe['ingredients']:
#         print(f"- {ingredient}")

# print(f"\n\nIngredients available across all recipes\n------------------------------\n")
# ingredients_list.sort()
# for ingredient in ingredients_list:
#     print(f"- {ingredient}")