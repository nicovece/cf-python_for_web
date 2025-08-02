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
            f"Cooking Time: {self.cooking_time}\n"
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
    print("\nCreating a new recipe:")
    name = input("Enter recipe name: ")
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
    print("\n" + "="*50)
    print("RECIPE SUMMARY")
    print("="*50)
    print(f"Name: {name}")
    print(f"Cooking Time: {cooking_time} minutes")
    print(f"Ingredients: {', '.join(ingredients)}")
    print(f"Difficulty: {difficulty}")
    print("="*50)
    
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
            print("4. Cancel editing")
            
            edit_choice = input("Enter your choice (1-4): ").strip()
            
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
            elif edit_choice == "4":
                continue
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Show updated summary
            print("\n" + "="*50)
            print("UPDATED RECIPE SUMMARY")
            print("="*50)
            print(f"Name: {name}")
            print(f"Cooking Time: {cooking_time} minutes")
            print(f"Ingredients: {', '.join(ingredients)}")
            print(f"Difficulty: {difficulty}")
            print("="*50)
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
        print("No recipes found in the database.")
        return
    
    print(f"Found {len(recipes)} recipe(s) in the database:")
    print("=" * 50)
    
    for i, recipe in enumerate(recipes, 1):
        print(f"\n--- Recipe {i} of {len(recipes)} ---")
        print(recipe.__str__())
        print("-" * 30)
    
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
            user_input = input("Enter your choice: ").strip()
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
            print(f"Searching for recipes containing: {', '.join(search_ingredients)}")
            break
            
        except ValueError:
            print("Please enter valid numbers separated by spaces.")
    
    # Initialize an empty list called conditions
    conditions = []
    
    # Run a loop through search_ingredients to create like conditions
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    
    # Retrieve all recipes using filter() query with the conditions
    matching_recipes = session.query(Recipe).filter(*conditions).all()
    
    # Display the results using __str__ method
    print(f"\nRecipes containing {', '.join(search_ingredients)}:")
    print("=" * 50)
    
    if matching_recipes:
        print(f"Found {len(matching_recipes)} matching recipe(s):")
        for i, recipe in enumerate(matching_recipes, 1):
            print(f"\n--- Recipe {i} of {len(matching_recipes)} ---")
            print(recipe.__str__())
            print("-" * 30)
        print(f"\nTotal: {len(matching_recipes)} recipe(s) found.")
    else:
        print(f"No recipes found containing {', '.join(search_ingredients)}.")
    
    input("\nPress Enter to return to main menu...")

def edit_recipe():
    print("\n=== Edit Recipe ===")
    
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
            choice = int(input(f"\nEnter the ID of the recipe to update: "))
            recipe_ids = [recipe.id for recipe in recipes]
            if choice in recipe_ids:
                recipe_to_update = next(recipe for recipe in recipes if recipe.id == choice)
                print(f"Updating recipe: {recipe_to_update.name}")
                break
            else:
                print(f"Please enter a valid recipe ID: {', '.join(map(str, recipe_ids))}")
        except ValueError:
            print("Please enter a valid number.")

    # Show current recipe details
    print(f"\nCurrent recipe details:")
    print(f"Name: {recipe_to_update.name}")
    print(f"Cooking Time: {recipe_to_update.cooking_time} minutes")
    print(f"Ingredients: {recipe_to_update.ingredients}")
    print(f"Difficulty: {recipe_to_update.difficulty}")
    
    # Update options menu
    while True:
        print("\n" + "-" * 30)
        print("What would you like to update?")
        print("1. Name")
        print("2. Cooking time")
        print("3. Ingredients")
        print("4. Cancel")

        update_choice = input("Enter your choice (1-4): ").strip()

        if update_choice == "1":
            new_name = input("Enter new recipe name: ").strip()
            if new_name:
                print(f"\nUpdate: '{recipe_to_update.name}' → '{new_name}'")
                confirm = input("Confirm this change? (y/n): ").strip().lower()
                if confirm in ['y', 'yes']:
                    try:
                        recipe_to_update.name = new_name
                        session.commit()
                        print(f"Recipe name updated successfully!")
                    except Exception as e:
                        print(f"Error updating recipe: {e}")
                        session.rollback()
                else:
                    print("Update cancelled.")
            else:
                print("Name cannot be empty.")
                
        elif update_choice == "2":
            while True:
                try:
                    new_cooking_time = int(input("Enter new cooking time (in minutes): "))
                    if new_cooking_time > 0:
                        # Recalculate difficulty
                        ingredients_list = recipe_to_update.return_ingredients_as_list()
                        # Create temporary recipe to calculate difficulty
                        temp_recipe = Recipe()
                        temp_recipe.cooking_time = new_cooking_time
                        temp_recipe.ingredients = ", ".join(ingredients_list)
                        temp_recipe.calc_difficulty()
                        new_difficulty = temp_recipe.difficulty
                        
                        print(f"\nUpdate: {recipe_to_update.cooking_time} minutes → {new_cooking_time} minutes")
                        print(f"Difficulty: {recipe_to_update.difficulty} → {new_difficulty}")
                        confirm = input("Confirm this change? (y/n): ").strip().lower()
                        
                        if confirm in ['y', 'yes']:
                            try:
                                recipe_to_update.cooking_time = new_cooking_time
                                recipe_to_update.difficulty = new_difficulty
                                session.commit()
                                print(f"Recipe cooking time and difficulty updated successfully!")
                            except Exception as e:
                                print(f"Error updating recipe: {e}")
                                session.rollback()
                        else:
                            print("Update cancelled.")
                        break
                    else:
                        print("Cooking time must be greater than 0.")
                except ValueError:
                    print("Please enter a valid integer for cooking time.")
                    
        elif update_choice == "3":
            current_ingredients = recipe_to_update.return_ingredients_as_list()
            print(f"\nCurrent ingredients: {', '.join(current_ingredients)}")
            print("\nWhat would you like to do with ingredients?")
            print("1. Replace all ingredients")
            print("2. Add new ingredients")
            print("3. Remove specific ingredients")
            print("4. Cancel")
            
            ingredient_choice = input("Enter your choice (1-4): ").strip()
            
            if ingredient_choice == "1":
                # Replace all ingredients
                new_ingredients_input = input("Enter new ingredients (comma separated): ").strip()
                if new_ingredients_input:
                    new_ingredients = [ingredient.strip() for ingredient in new_ingredients_input.split(",")]
                    new_ingredients_str = ", ".join(new_ingredients)
                    
                    # Recalculate difficulty
                    temp_recipe = Recipe()
                    temp_recipe.cooking_time = recipe_to_update.cooking_time
                    temp_recipe.ingredients = new_ingredients_str
                    temp_recipe.calc_difficulty()
                    new_difficulty = temp_recipe.difficulty
                    
                    print(f"\nUpdate: '{recipe_to_update.ingredients}' → '{new_ingredients_str}'")
                    print(f"Difficulty: {recipe_to_update.difficulty} → {new_difficulty}")
                    confirm = input("Confirm this change? (y/n): ").strip().lower()
                    
                    if confirm in ['y', 'yes']:
                        try:
                            recipe_to_update.ingredients = new_ingredients_str
                            recipe_to_update.difficulty = new_difficulty
                            session.commit()
                            print(f"Recipe ingredients and difficulty updated successfully!")
                        except Exception as e:
                            print(f"Error updating recipe: {e}")
                            session.rollback()
                    else:
                        print("Update cancelled.")
                else:
                    print("Ingredients cannot be empty.")
                    
            elif ingredient_choice == "2":
                # Add new ingredients
                print(f"\nCurrent ingredients: {', '.join(current_ingredients)}")
                add_ingredients_input = input("Enter ingredients to add (comma separated): ").strip()
                if add_ingredients_input:
                    ingredients_to_add = [ingredient.strip() for ingredient in add_ingredients_input.split(",")]
                    # Combine current and new ingredients, avoiding duplicates
                    combined_ingredients = current_ingredients.copy()
                    for ingredient in ingredients_to_add:
                        if ingredient.lower() not in [ing.lower() for ing in combined_ingredients]:
                            combined_ingredients.append(ingredient)
                    
                    new_ingredients_str = ", ".join(combined_ingredients)
                    
                    # Recalculate difficulty
                    temp_recipe = Recipe()
                    temp_recipe.cooking_time = recipe_to_update.cooking_time
                    temp_recipe.ingredients = new_ingredients_str
                    temp_recipe.calc_difficulty()
                    new_difficulty = temp_recipe.difficulty
                    
                    print(f"\nUpdate: '{recipe_to_update.ingredients}' → '{new_ingredients_str}'")
                    print(f"Difficulty: {recipe_to_update.difficulty} → {new_difficulty}")
                    confirm = input("Confirm this change? (y/n): ").strip().lower()
                    
                    if confirm in ['y', 'yes']:
                        try:
                            recipe_to_update.ingredients = new_ingredients_str
                            recipe_to_update.difficulty = new_difficulty
                            session.commit()
                            print(f"Recipe ingredients and difficulty updated successfully!")
                        except Exception as e:
                            print(f"Error updating recipe: {e}")
                            session.rollback()
                    else:
                        print("Update cancelled.")
                else:
                    print("No ingredients to add.")
                    
            elif ingredient_choice == "3":
                # Remove specific ingredients
                if len(current_ingredients) <= 1:
                    print("Cannot remove ingredients - recipe must have at least one ingredient.")
                    continue
                    
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
                        
                        # Recalculate difficulty
                        temp_recipe = Recipe()
                        temp_recipe.cooking_time = recipe_to_update.cooking_time
                        temp_recipe.ingredients = new_ingredients_str
                        temp_recipe.calc_difficulty()
                        new_difficulty = temp_recipe.difficulty
                        
                        print(f"\nUpdate: '{recipe_to_update.ingredients}' → '{new_ingredients_str}'")
                        print(f"Difficulty: {recipe_to_update.difficulty} → {new_difficulty}")
                        confirm = input("Confirm this change? (y/n): ").strip().lower()
                        
                        if confirm in ['y', 'yes']:
                            try:
                                recipe_to_update.ingredients = new_ingredients_str
                                recipe_to_update.difficulty = new_difficulty
                                session.commit()
                                print(f"Recipe ingredients and difficulty updated successfully!")
                            except Exception as e:
                                print(f"Error updating recipe: {e}")
                                session.rollback()
                        else:
                            print("Update cancelled.")
                        break  # Exit the loop after processing
                        
                    except ValueError:
                        print("Please enter valid numbers separated by commas.")
                        continue  # Ask again for valid input
                    
            elif ingredient_choice == "4":
                print("Returning to edit menu...")
                continue
            else:
                print("Invalid choice. Please try again.")
                
        elif update_choice == "4":
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
    print(f"Name: {recipe_to_delete.name}")
    print(f"Cooking Time: {recipe_to_delete.cooking_time} minutes")
    print(f"Ingredients: {recipe_to_delete.ingredients}")
    print(f"Difficulty: {recipe_to_delete.difficulty}")
    
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
        print("\n=== Recipe Management System ===")
        print("1. Create recipe")
        print("2. View all recipes")
        print("3. Search recipe")
        print("4. Update recipe")
        print("5. Delete recipe")
        print("6. Exit (or type 'quit')")
        
        choice = input("Enter your choice: ").strip().lower()
        
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
        elif choice in ["6", "quit", "exit", "q"]:
            print("Goodbye!")
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()