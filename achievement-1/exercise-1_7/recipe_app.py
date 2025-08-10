from sqlalchemy import create_engine, select, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv 

Base = declarative_base()

# Load environment variables from .env file
script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, '.env'))

# Create database connection string from environment variables
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    def __str__(self):
        return (
            f"Recipe ID: {self.id}\n"
            f"Recipe Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking Time: {self.cooking_time} minutes\n"
            f"Difficulty: {self.difficulty}"
        )
    
    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return [ingredient.strip() for ingredient in self.ingredients.split(", ")]
    
    def calc_difficulty(self):
        # Use the helper method to get ingredients as a list
        ingredients_list = self.return_ingredients_as_list()
        num_ingredients = len(ingredients_list)
        
        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and num_ingredients >= 4:
            self.difficulty = "Hard"

Base.metadata.create_all(engine)

def create_recipe():
    print("\n=== Create Recipe ===")
    name = input("\nEnter recipe name: ")
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("\nPlease enter a valid integer for the cooking time.")
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients (comma separated): ").split(",")]
    
    # Create a temporary Recipe object to calculate difficulty
    temp_recipe = Recipe()
    temp_recipe.cooking_time = cooking_time
    temp_recipe.ingredients = ", ".join(ingredients)
    temp_recipe.calc_difficulty()
    difficulty = temp_recipe.difficulty
    
    # Show recipe summary and ask for confirmation
    print("\nRECIPE SUMMARY")
    # Create temporary recipe to display using __str__
    temp_recipe = Recipe()
    temp_recipe.name = name
    temp_recipe.cooking_time = cooking_time
    temp_recipe.ingredients = ", ".join(ingredients)
    temp_recipe.difficulty = difficulty
    print(temp_recipe.__str__())
    
    while True:
        confirm = input("\nIs this correct? (y/n/edit): ").strip().lower()
        
        if confirm in ['y', 'yes', '']:
            # User confirmed - proceed to save
            break
        elif confirm in ['n', 'no']:
            print("Recipe creation cancelled.")
            return
        elif confirm in ['e', 'edit']:
            # Allow editing
            print("\nWhat would you like to edit?")
            print("1. Name")
            print("2. Cooking time")
            print("3. Ingredients")
            print("0. Cancel editing")
            
            edit_choice = input("Enter your choice (0-3): ").strip()
            
            if edit_choice == "1":
                name = input("Enter new recipe name: ")
            elif edit_choice == "2":
                while True:
                    try:
                        cooking_time = int(input("Enter new cooking time (in minutes): "))
                        break
                    except ValueError:
                        print("Please enter a valid integer for the cooking time.")
                # Create temporary recipe to calculate difficulty
                temp_recipe = Recipe()
                temp_recipe.cooking_time = cooking_time
                temp_recipe.ingredients = ", ".join(ingredients)
                temp_recipe.calc_difficulty()
                difficulty = temp_recipe.difficulty
            elif edit_choice == "3":
                ingredients = [ingredient.strip() for ingredient in input("Enter new ingredients (comma separated): ").split(",")]
                # Create temporary recipe to calculate difficulty
                temp_recipe = Recipe()
                temp_recipe.cooking_time = cooking_time
                temp_recipe.ingredients = ", ".join(ingredients)
                temp_recipe.calc_difficulty()
                difficulty = temp_recipe.difficulty
            elif edit_choice == "0":
                continue
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Show updated summary
            print("\nUPDATED RECIPE SUMMARY")
            # Create temporary recipe to display using __str__
            temp_recipe = Recipe()
            temp_recipe.name = name
            temp_recipe.cooking_time = cooking_time
            temp_recipe.ingredients = ", ".join(ingredients)
            temp_recipe.difficulty = difficulty
            print(temp_recipe.__str__())
        else:
            print("Please enter 'y' to confirm, 'n' to cancel, or 'edit' to modify.")
    
    # Convert ingredients list to string for storage
    ingredients_str = ", ".join(ingredients)
    
    # Create and save the recipe using SQLAlchemy
    try:
        new_recipe = Recipe(name=name, cooking_time=cooking_time, ingredients=ingredients_str, difficulty=difficulty)
        session.add(new_recipe)
        session.commit()
        print(f"\nRecipe '{name}' created successfully!")
    except Exception as e:
        print(f"Error creating recipe: {e}")
        session.rollback()

def view_all_recipes():
    print("\n=== View All Recipes ===")
    recipes = session.query(Recipe).all()
    if not recipes:
        print("\nNo recipes found in the database.")
        return
    
    print(f"\nFound {len(recipes)} recipe(s) in the database:")
    for i, recipe in enumerate(recipes, 1):
        print(f"\n--- Recipe {i} of {len(recipes)} ---")
        print(recipe.__str__())
    
    print(f"\nTotal: {len(recipes)} recipe(s) displayed.")
    input("\nPress Enter to return to main menu...")

def search_recipe():
    print("\n=== Recipe Search ===")
    
    # Check if your table has any entries using count() method
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return
    
    # Retrieve only the values from the ingredients column
    results = session.query(Recipe.ingredients).all()
    
    # Initialize an empty list called all_ingredients
    all_ingredients = []
    
    # Go through each entry in results, split up the ingredients, and add to all_ingredients
    for result in results:
        ingredients_string = result[0]  # Get the ingredients string from the result tuple
        ingredients_list = [ingredient.strip().lower() for ingredient in ingredients_string.split(", ")]
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display ingredients to the user with numbers
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient.title()}")
    
    # Ask user to pick ingredients by numbers, separated by spaces
    print(f"\nEnter the numbers of ingredients to search for (1-{len(all_ingredients)}), separated by spaces:")
    print("Example: 1 3 5")
    print("Or enter '0' to return to main menu")
    
    while True:
        try:
            user_input = input("\nEnter your choice: ").strip()
            if user_input == "0":
                print("Returning to main menu...")
                return
            
            # Parse the user input into a list of numbers
            choice_numbers = [int(x) for x in user_input.split()]
            
            # Check that all numbers are valid
            valid_choices = all(1 <= num <= len(all_ingredients) for num in choice_numbers)
            if not valid_choices:
                print(f"Please enter numbers between 1 and {len(all_ingredients)}.")
                continue
            
            # Create search_ingredients list based on user selection
            search_ingredients = [all_ingredients[num - 1] for num in choice_numbers]
            print(f"\nSearching for recipes containing: {', '.join(search_ingredients)}")
            break
            
        except ValueError:
            print("Please enter valid numbers separated by spaces.")
    
    # Initialize an empty list called conditions
    conditions = []
    
    # Run a loop through search_ingredients to create ilike conditions (case-insensitive)
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.ilike(like_term))
    
    # Retrieve all recipes using filter() query with the conditions
    matching_recipes = session.query(Recipe).filter(*conditions).all()
    
    # Display the results using __str__ method
    print(f"\nRecipes containing {', '.join(search_ingredients)}:")
    print("-" * 30)
    
    if matching_recipes:
        print(f"Found {len(matching_recipes)} matching recipe(s)")
        for i, recipe in enumerate(matching_recipes, 1):
            print(f"\n--- Recipe {i} of {len(matching_recipes)} ---")
            print(recipe.__str__())
        print(f"\nTotal: {len(matching_recipes)} recipe(s) found.")
    else:
        print(f"No recipes found containing {', '.join(search_ingredients)}.")
    
    input("\nPress Enter to return to main menu...")

def edit_recipe():
    print("\n=== Edit Recipe ===")
    # Check if any recipes exist on your database, and continue only if there are any
    recipe_count = session.query(Recipe).count()
    if recipe_count == 0:
        print("No recipes found in the database.")
        return
    
    # Retrieve the id and name for each recipe from the database, and store them into results
    results = session.query(Recipe.id, Recipe.name).all()
    
    # From each item in results, display the recipes available to the user
    print("\nAvailable recipes:")
    for result in results:
        print(f"ID {result[0]}: {result[1]}")
    
    # The user gets to pick a recipe by its id. If the chosen id doesn't exist, exit the function
    try:
        choice = int(input("\nEnter the ID of the recipe to edit: "))
        # Check if the chosen id exists
        recipe_ids = [result[0] for result in results]
        if choice not in recipe_ids:
            print(f"Recipe ID {choice} does not exist.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Retrieve the entire recipe that corresponds to this id from the database
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == choice).first()
    
    # Main editing loop - keep user in editing menu
    while True:
        # Display the recipe using __str__ method for consistency
        print(f"\nRecipe to edit:")
        print(recipe_to_edit.__str__())
        print("\nWhat would you like to edit?")
        print("1. Name")
        print("2. Ingredients")
        print("3. Cooking Time")
        print("0. Done editing (return to main menu)")
        
        # Ask the user which attribute they'd like to edit by entering the corresponding number
        while True:
            try:
                attribute_choice = int(input("\nEnter the number of the attribute to edit (0-3): "))
                if 0 <= attribute_choice <= 3:
                    break
                else:
                    print("Please enter a number between 0 and 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Based on the input, use if-else statements to edit the respective attribute
        if attribute_choice == 1:
            # Edit name
            new_name = input("Enter new recipe name: ").strip()
            if new_name:
                # Show confirmation with old vs new
                print(f"\nUpdate: '{recipe_to_edit.name}' → '{new_name}'")
                confirm = input("Confirm this change? (y/n): ").strip().lower()
                if confirm in ['y', 'yes']:
                    recipe_to_edit.name = new_name
                    # Recalculate the difficulty using the object's calc_difficulty() method
                    recipe_to_edit.calc_difficulty()
                    # Commit these changes to the database
                    session.commit()
                    print("Recipe name updated successfully!")
                else:
                    print("Update cancelled.")
            else:
                print("Name cannot be empty.")
                
        elif attribute_choice == 2:
            # Edit ingredients with enhanced UX
            current_ingredients = recipe_to_edit.return_ingredients_as_list()
            print(f"\nCurrent ingredients: {', '.join(current_ingredients)}")
            print("\nWhat would you like to do with ingredients?")
            print("1. Replace all ingredients")
            print("2. Add new ingredients")
            print("3. Remove specific ingredients")
            print("0. Cancel")
            
            ingredient_choice = input("Enter your choice (0-3): ").strip()
            
            if ingredient_choice == "1":
                # Replace all ingredients (follows exercise directions)
                new_ingredients = input("Enter new ingredients (comma separated): ").strip()
                if new_ingredients:
                    # Show confirmation with old vs new
                    print(f"\nUpdate: '{recipe_to_edit.ingredients}' → '{new_ingredients}'")
                    confirm = input("Confirm this change? (y/n): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        recipe_to_edit.ingredients = new_ingredients
                        # Recalculate the difficulty using the object's calc_difficulty() method
                        recipe_to_edit.calc_difficulty()
                        # Commit these changes to the database
                        session.commit()
                        print("Recipe ingredients updated successfully!")
                    else:
                        print("Update cancelled.")
                else:
                    print("Ingredients cannot be empty.")
                    
            elif ingredient_choice == "2":
                # Add new ingredients (UX improvement)
                add_ingredients_input = input("Enter ingredients to add (comma separated): ").strip()
                if add_ingredients_input:
                    ingredients_to_add = [ingredient.strip() for ingredient in add_ingredients_input.split(",")]
                    # Combine current and new ingredients, avoiding duplicates
                    combined_ingredients = current_ingredients.copy()
                    for ingredient in ingredients_to_add:
                        if ingredient.lower() not in [ing.lower() for ing in combined_ingredients]:
                            combined_ingredients.append(ingredient)
                    
                    new_ingredients_str = ", ".join(combined_ingredients)
                    
                    # Show confirmation with old vs new
                    print(f"\nUpdate: '{recipe_to_edit.ingredients}' → '{new_ingredients_str}'")
                    confirm = input("Confirm this change? (y/n): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        recipe_to_edit.ingredients = new_ingredients_str
                        # Recalculate the difficulty using the object's calc_difficulty() method
                        recipe_to_edit.calc_difficulty()
                        # Commit these changes to the database
                        session.commit()
                        print("Recipe ingredients updated successfully!")
                    else:
                        print("Update cancelled.")
                else:
                    print("No ingredients to add.")
                    
            elif ingredient_choice == "3":
                # Remove specific ingredients (UX improvement)
                if len(current_ingredients) <= 1:
                    print("Cannot remove ingredients - recipe must have at least one ingredient.")
                else:
                    print(f"\nCurrent ingredients:")
                    for i, ingredient in enumerate(current_ingredients, 1):
                        print(f"{i}. {ingredient}")
                    
                    # Loop to keep asking for valid input
                    while True:
                        remove_input = input("Enter the numbers of ingredients to remove (comma separated): ").strip()
                        if not remove_input:
                            print("No ingredients to remove.")
                            break
                        
                        try:
                            remove_indices = [int(x.strip()) - 1 for x in remove_input.split(",")]
                            # Validate indices
                            valid_indices = all(0 <= idx < len(current_ingredients) for idx in remove_indices)
                            if not valid_indices:
                                print("Invalid ingredient numbers. Please try again.")
                                continue
                            
                            # Remove ingredients
                            remaining_ingredients = [ing for i, ing in enumerate(current_ingredients) if i not in remove_indices]
                            
                            if not remaining_ingredients:
                                print("Cannot remove all ingredients - recipe must have at least one ingredient.")
                                break
                            
                            new_ingredients_str = ", ".join(remaining_ingredients)
                            
                            # Show confirmation with old vs new
                            print(f"\nUpdate: '{recipe_to_edit.ingredients}' → '{new_ingredients_str}'")
                            confirm = input("Confirm this change? (y/n): ").strip().lower()
                            if confirm in ['y', 'yes']:
                                recipe_to_edit.ingredients = new_ingredients_str
                                # Recalculate the difficulty using the object's calc_difficulty() method
                                recipe_to_edit.calc_difficulty()
                                # Commit these changes to the database
                                session.commit()
                                print("Recipe ingredients updated successfully!")
                            else:
                                print("Update cancelled.")
                            break
                            
                        except ValueError:
                            print("Please enter valid numbers separated by commas.")
                            continue
                            
            elif ingredient_choice == "0":
                print("Returning to attribute selection...")
            else:
                print("Invalid choice. Please try again.")
                
        elif attribute_choice == 3:
            # Edit cooking time
            try:
                new_cooking_time = int(input("Enter new cooking time (in minutes): "))
                if new_cooking_time > 0:
                    # Show confirmation with old vs new
                    print(f"\nUpdate: {recipe_to_edit.cooking_time} minutes → {new_cooking_time} minutes")
                    confirm = input("Confirm this change? (y/n): ").strip().lower()
                    if confirm in ['y', 'yes']:
                        recipe_to_edit.cooking_time = new_cooking_time
                        # Recalculate the difficulty using the object's calc_difficulty() method
                        recipe_to_edit.calc_difficulty()
                        # Commit these changes to the database
                        session.commit()
                        print("Recipe cooking time updated successfully!")
                    else:
                        print("Update cancelled.")
                else:
                    print("Cooking time must be greater than 0.")
            except ValueError:
                print("Please enter a valid integer for cooking time.")
                
        elif attribute_choice == 0:
            # Done editing - return to main menu
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def delete_recipe():
    print("\n=== Recipe Delete ===")
    # Get all recipes from database
    recipes = session.query(Recipe).all()
    
    if not recipes:
        print("No recipes found in the database.")
        print("Please create some recipes first.")
        return
    
    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"ID {recipe.id}: {recipe.name}")

    # Get recipe selection from user
    while True:
        try:
            choice = int(input(f"\nEnter the ID of the recipe to delete: "))
            recipe_ids = [recipe.id for recipe in recipes]
            if choice in recipe_ids:
                recipe_to_delete = next(recipe for recipe in recipes if recipe.id == choice)
                break
            else:
                print(f"Please enter a valid recipe ID: {', '.join(map(str, recipe_ids))}")
        except ValueError:
            print("Please enter a valid number.")

    # Show recipe details and ask for confirmation
    print(f"\nRecipe to delete:")
    print(recipe_to_delete.__str__())
    
    confirm = input(f"\nAre you sure you want to delete '{recipe_to_delete.name}'? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes']:
        try:
            session.delete(recipe_to_delete)
            session.commit()
            print(f"Recipe '{recipe_to_delete.name}' deleted successfully!")
        except Exception as e:
            print(f"Error deleting recipe: {e}")
            session.rollback()
    else:
        print("Deletion cancelled.")

def main_menu():
    while True:
        print("\n=== Recipe Management System ===\n")
        print("1. Create recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("0. Exit (or type 'quit' or 'q')")
        
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice in ["1", "create", "add"]:
            create_recipe()
        elif choice in ["2", "view", "list", "all"]:
            view_all_recipes()
        elif choice in ["3", "search", "find"]:
            search_recipe()
        elif choice in ["4", "update", "edit"]:
            edit_recipe()
        elif choice in ["5", "delete", "remove"]:
            delete_recipe()
        elif choice in ["0", "quit", "exit", "q"]:
            print("Goodbye!")
            session.close()
            engine.dispose()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()