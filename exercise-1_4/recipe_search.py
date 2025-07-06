import pickle
import os

def display_recipe(recipe):
    print(f"\n---\n\nRecipe: {recipe['name']}")
    print(f"Cooking time: {recipe['cooking_time']}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")

def search_ingredient(data):
    available_ingredients = list(enumerate(data['all_ingredients'], 1))
    print("\n---\n\nAvailable ingredients:")
    for index, ingredient in available_ingredients:
        print(f"{index}. {ingredient}")

    try:
        ingredient_index = int(input("\n---\n\nEnter the number of the ingredient you want to search for: "))
        ingredient_searched = available_ingredients[ingredient_index - 1][1]
        print(f"\n---\n\nSearching for recipes with {ingredient_searched}...")
    except ValueError:
        print("\n---\n\nInvalid input. Please enter a valid number.")
    except IndexError:
        print("\n---\n\nYour input is not a valid ingredient number. Please try again.")
    else:
        found = False
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
                found = True
        if not found:
            print("\n---\n\nNo recipes found with that ingredient.")

script_dir = os.path.dirname(__file__)
filename = input("\n---\nEnter the filename where your recipes are stored: ")
if not filename.endswith('.bin'):
    filename += '.bin'
filepath = os.path.join(script_dir, filename)

try:
    with open(filepath, 'rb') as file:
        data = pickle.load(file)
        print("\n---\n\nData loaded successfully from file.")
except FileNotFoundError:
    print(f"\n---\n\nNo file found with the name {filename}. Please try again.")
except Exception as error:
    print(f"\n---\n\nAn error occurred while loading the file: {error}")
else:
    search_ingredient(data)