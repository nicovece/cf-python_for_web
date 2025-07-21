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
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    
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
    
    # Convert ingredients list to string for MySQL storage
    ingredients_str = ", ".join(ingredients)
    
    # Create the recipes table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            cooking_time INT NOT NULL,
            ingredients TEXT NOT NULL,
            difficulty VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert the recipe into the database
    sql = """INSERT INTO recipes (name, cooking_time, ingredients, difficulty) 
             VALUES (%s, %s, %s, %s)"""
    values = (name, cooking_time, ingredients_str, difficulty)
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"\nRecipe '{name}' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating recipe: {err}")
        conn.rollback()

def search_recipe(conn, cursor):
    print("Searching recipe...")

def update_recipe(conn, cursor):
    print("Updating recipe...")

def delete_recipe(conn, cursor):
    print("Deleting recipe...")

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