import pickle
import os

def display_recipe(recipe):
    print(f"\n---\nRecipe: {recipe['name']}")
    print(f"Cooking time: {recipe['cooking_time']}")
    print(f"Difficulty: {recipe['difficulty']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")

def main():
    script_dir = os.path.dirname(__file__)
    filename = input("\n---\nEnter the filename where your recipes are stored: ")
    if not filename.endswith('.bin'):
        filename += '.bin'
    filepath = os.path.join(script_dir, filename)

    try:
        with open(filepath, 'rb') as file:
            data = pickle.load(file)
            print("\n---\nData loaded successfully from file.")
    except FileNotFoundError:
        print(f"\n---\nNo file found with the name {filename}. Please try again.")
        return
    except Exception as error:
        print(f"\n---\nAn error occurred while loading the file: {error}")
        return

    recipes = data.get('recipes_list', [])
    if not recipes:
        print("\n---\nNo recipes found in the file.")
        return

    print(f"\n---\nFound {len(recipes)} recipe(s):")
    for recipe in recipes:
        display_recipe(recipe)

if __name__ == "__main__":
    main() 