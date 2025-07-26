import mysql.connector
import os
from dotenv import load_dotenv

def get_database_connection():
    # Get a connection to the MySQL database
    # Load .env file from the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(script_dir, '.env'))
    
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        database='task_database')

def create_database():
    # Create the task_database if it doesn't exist
    # Load .env file from the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(script_dir, '.env'))
    
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'))
    
    cursor = conn.cursor()
    # Build query as string and execute
    create_db_query = "CREATE DATABASE IF NOT EXISTS task_database"
    cursor.execute(create_db_query)
    
    cursor.close()
    conn.close()
    print("Database 'task_database' created successfully!")

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

def create_recipe(conn, cursor):
    print("\nCreating a new recipe:")
    name = input("Enter recipe name: ")
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("\nPlease enter a valid integer for the cooking time.")
    ingredients = [ingredient.strip() for ingredient in input("Enter ingredients (comma separated): ").split(",")]
    difficulty = calc_difficulty(cooking_time, ingredients)
    
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
                difficulty = calc_difficulty(cooking_time, ingredients)
            elif edit_choice == "3":
                ingredients = [ingredient.strip() for ingredient in input("Enter new ingredients (comma separated): ").split(",")]
                difficulty = calc_difficulty(cooking_time, ingredients)
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
    
    # Convert ingredients list to string for MySQL storage
    ingredients_str = ", ".join(ingredients)
    
    # Create the recipes table if it doesn't exist
    create_table_query = """
        CREATE TABLE IF NOT EXISTS recipes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            cooking_time INT NOT NULL,
            ingredients TEXT NOT NULL,
            difficulty VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    cursor.execute(create_table_query)
    
    # Insert the recipe into the database
    sql = """INSERT INTO recipes (name, cooking_time, ingredients, difficulty) VALUES (%s, %s, %s, %s)"""
    values = (name, cooking_time, ingredients_str, difficulty)
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"\nRecipe '{name}' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating recipe: {err}")
        conn.rollback()

def search_recipe(conn, cursor):
    print("\n=== Recipe Search ===")
    
    # Step 1: SELECT only the ingredients column from the table
    select_query = "SELECT ingredients FROM recipes"
    cursor.execute(select_query)
    results = cursor.fetchall()
    
    # Step 2: Create a list to store all ingredients without duplicates
    all_ingredients = []
    
    # Process each row (tuple) from results
    for result in results:
        # Each result is a tuple with one element (the ingredients string)
        ingredients_string = result[0]
        # Split the ingredients string by comma and space
        ingredients_list = ingredients_string.split(", ")
        
        # Add each ingredient to all_ingredients if not already present
        for ingredient in ingredients_list:
            ingredient_clean = ingredient.strip().lower()
            if ingredient_clean not in all_ingredients:
                all_ingredients.append(ingredient_clean)
    
    # Step 3: Display all ingredients to the user with numbers
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient.title()}")
    
    # Step 4: Allow user to pick an ingredient by number
    print(f"\nEnter the number of the ingredient to search for (1-{len(all_ingredients)}):")
    print("Or enter '0' to return to main menu")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Returning to main menu...")
                return
            elif 1 <= choice <= len(all_ingredients):
                search_ingredient = all_ingredients[choice - 1]
                print(f"Searching for: '{search_ingredient}'")  # Debug line
                break
            else:
                print(f"Please enter a number between 0 and {len(all_ingredients)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Step 5: Search for recipes containing the selected ingredient
    search_query = """
        SELECT name, cooking_time, ingredients, difficulty 
        FROM recipes 
        WHERE LOWER(ingredients) LIKE %s
    """
    cursor.execute(search_query, (f'%{search_ingredient}%',))
    
    matching_recipes = cursor.fetchall()
    
    # Display the results
    print(f"\nRecipes containing '{search_ingredient}':")
    print("=" * 50)
    
    if matching_recipes:
        for recipe in matching_recipes:
            print(f"\nRecipe: {recipe[0]}")
            print(f"Cooking Time: {recipe[1]} minutes")
            print(f"Ingredients: {recipe[2]}")
            print(f"Difficulty: {recipe[3]}")
            print("-" * 30)
    else:
        print(f"No recipes found containing '{search_ingredient}'.")
    
    # Ask user if they want to search again or return to main menu
    while True:
        print("\n" + "-" * 30)
        print("\nWhat would you like to do?")
        print("1. Search for another ingredient")
        print("2. Return to main menu")
        
        search_choice = input("Enter your choice (1-2): ").strip()
        
        if search_choice == "1":
            # Recursively call search_recipe to search again
            search_recipe(conn, cursor)
            break
        elif search_choice == "2":
            print("Returning to main menu...")
            break
        else:
            print("Please enter 1 or 2.")



def update_recipe(conn, cursor):
    print("\n=== Recipe Update ===")
    
    # Check if there are any recipes to update
    select_query = "SELECT id, name FROM recipes"
    cursor.execute(select_query)
    recipes = cursor.fetchall()
    
    if not recipes:
        print("No recipes found in the database.")
        print("Please create some recipes first.")
        return
    
    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"ID {recipe[0]}: {recipe[1]}")

    # Get recipe selection from user
    while True:
        try:
            choice = int(input(f"\nEnter the ID of the recipe to update: "))
            # Check if the entered ID exists in our recipes list
            recipe_ids = [recipe[0] for recipe in recipes]
            if choice in recipe_ids:
                recipe_id = choice
                recipe_name = next(recipe[1] for recipe in recipes if recipe[0] == choice)
                print(f"Updating recipe: {recipe_name}")
                break
            else:
                print(f"Please enter a valid recipe ID: {', '.join(map(str, recipe_ids))}")
        except ValueError:
            print("Please enter a valid number.")

    # Get current recipe data
    select_query = "SELECT name, cooking_time, ingredients, difficulty FROM recipes WHERE id = %s"
    cursor.execute(select_query, (recipe_id,))
    current_recipe = cursor.fetchone()
    
    if not current_recipe:
        print("Recipe not found!")
        return
    
    current_name, current_cooking_time, current_ingredients, current_difficulty = current_recipe
    
    # Show current recipe details
    print(f"\nCurrent recipe details:")
    print(f"Name: {current_name}")
    print(f"Cooking Time: {current_cooking_time} minutes")
    print(f"Ingredients: {current_ingredients}")
    print(f"Difficulty: {current_difficulty}")
    
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
                # Show confirmation
                print(f"\nUpdate: '{current_name}' → '{new_name}'")
                confirm = input("Confirm this change? (y/n): ").strip().lower()
                if confirm in ['y', 'yes']:
                    try:
                        # Build query as string and execute
                        update_query = "UPDATE recipes SET name = %s WHERE id = %s"
                        cursor.execute(update_query, (new_name, recipe_id))
                        conn.commit()
                        print(f"Recipe name updated successfully!")
                    except mysql.connector.Error as err:
                        print(f"Error updating recipe: {err}")
                        conn.rollback()
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
                        ingredients_list = current_ingredients.split(", ")
                        new_difficulty = calc_difficulty(new_cooking_time, ingredients_list)
                        
                        # Show confirmation
                        print(f"\nUpdate: {current_cooking_time} minutes → {new_cooking_time} minutes")
                        print(f"Difficulty: {current_difficulty} → {new_difficulty}")
                        confirm = input("Confirm this change? (y/n): ").strip().lower()
                        
                        if confirm in ['y', 'yes']:
                            try:
                                # Build query as string and execute (separate queries as per exercise)
                                update_query = "UPDATE recipes SET cooking_time = %s WHERE id = %s"
                                cursor.execute(update_query, (new_cooking_time, recipe_id))
                                
                                # Separate query for difficulty update
                                difficulty_query = "UPDATE recipes SET difficulty = %s WHERE id = %s"
                                cursor.execute(difficulty_query, (new_difficulty, recipe_id))
                                
                                conn.commit()
                                print(f"Recipe cooking time and difficulty updated successfully!")
                            except mysql.connector.Error as err:
                                print(f"Error updating recipe: {err}")
                                conn.rollback()
                        else:
                            print("Update cancelled.")
                        break
                    else:
                        print("Cooking time must be greater than 0.")
                except ValueError:
                    print("Please enter a valid integer for cooking time.")
                    
        elif update_choice == "3":
            new_ingredients_input = input("Enter new ingredients (comma separated): ").strip()
            if new_ingredients_input:
                new_ingredients = [ingredient.strip() for ingredient in new_ingredients_input.split(",")]
                new_ingredients_str = ", ".join(new_ingredients)
                
                # Recalculate difficulty
                new_difficulty = calc_difficulty(current_cooking_time, new_ingredients)
                
                # Show confirmation
                print(f"\nUpdate: '{current_ingredients}' → '{new_ingredients_str}'")
                print(f"Difficulty: {current_difficulty} → {new_difficulty}")
                confirm = input("Confirm this change? (y/n): ").strip().lower()
                
                if confirm in ['y', 'yes']:
                    try:
                        # Build query as string and execute (separate queries as per exercise)
                        update_query = "UPDATE recipes SET ingredients = %s WHERE id = %s"
                        cursor.execute(update_query, (new_ingredients_str, recipe_id))
                        
                        # Separate query for difficulty update
                        difficulty_query = "UPDATE recipes SET difficulty = %s WHERE id = %s"
                        cursor.execute(difficulty_query, (new_difficulty, recipe_id))
                        
                        conn.commit()
                        print(f"Recipe ingredients and difficulty updated successfully!")
                    except mysql.connector.Error as err:
                        print(f"Error updating recipe: {err}")
                        conn.rollback()
                else:
                    print("Update cancelled.")
            else:
                print("Ingredients cannot be empty.")
                
        elif update_choice == "4":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def delete_recipe(conn, cursor):
    print("\n=== Recipe Delete ===")
    
    # Check if there are any recipes to delete
    select_query = "SELECT id, name FROM recipes"
    cursor.execute(select_query)
    recipes = cursor.fetchall()
    
    if not recipes:
        print("No recipes found in the database.")
        print("Please create some recipes first.")
        return
    
    print("\nAvailable recipes:")
    for recipe in recipes:
        print(f"ID {recipe[0]}: {recipe[1]}")

    # Get recipe selection from user
    while True:
        try:
            choice = int(input(f"\nEnter the ID of the recipe to delete: "))
            # Check if the entered ID exists in our recipes list
            recipe_ids = [recipe[0] for recipe in recipes]
            if choice in recipe_ids:
                recipe_id = choice
                recipe_name = next(recipe[1] for recipe in recipes if recipe[0] == choice)
                break
            else:
                print(f"Please enter a valid recipe ID: {', '.join(map(str, recipe_ids))}")
        except ValueError:
            print("Please enter a valid number.")

    # Get current recipe data to show before deletion
    select_query = "SELECT name, cooking_time, ingredients, difficulty FROM recipes WHERE id = %s"
    cursor.execute(select_query, (recipe_id,))
    current_recipe = cursor.fetchone()
    
    if not current_recipe:
        print("Recipe not found!")
        return
    
    current_name, current_cooking_time, current_ingredients, current_difficulty = current_recipe
    
    # Show recipe details and ask for confirmation
    print(f"\nRecipe to delete:")
    print(f"Name: {current_name}")
    print(f"Cooking Time: {current_cooking_time} minutes")
    print(f"Ingredients: {current_ingredients}")
    print(f"Difficulty: {current_difficulty}")
    
    confirm = input(f"\nAre you sure you want to delete '{current_name}'? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes']:
        try:
            # Build query as string and execute
            delete_query = "DELETE FROM recipes WHERE id = %s"
            cursor.execute(delete_query, (recipe_id,))
            conn.commit()
            print(f"Recipe '{current_name}' deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error deleting recipe: {err}")
            conn.rollback()
    else:
        print("Deletion cancelled.")

def main_menu(conn, cursor):
    while True:
        print("\n=== Recipe Management System ===")
        print("1. Create recipe")
        print("2. Search recipe")
        print("3. Update recipe")
        print("4. Delete recipe")
        print("5. Exit (or type 'quit')")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice in ["1", "create", "add"]:
            create_recipe(conn, cursor)
        elif choice in ["2", "search", "find"]:
            search_recipe(conn, cursor)
        elif choice in ["3", "update", "edit"]:
            update_recipe(conn, cursor)
        elif choice in ["4", "delete", "remove"]:
            delete_recipe(conn, cursor)
        elif choice in ["5", "quit", "exit", "q"]:
            print("Goodbye!")
            conn.commit()
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    create_database()  # Create the database first
    conn = get_database_connection()
    cursor = conn.cursor()
    main_menu(conn, cursor)