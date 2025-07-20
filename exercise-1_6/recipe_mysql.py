import mysql.connector
import os
from dotenv import load_dotenv

def get_database_connection():
    # Get a connection to the MySQL database
    load_dotenv()
    
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        database='task_database')

def create_database():
    # Create the task_database if it doesn't exist
    load_dotenv()
    
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'))
    
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
    
    cursor.close()
    conn.close()
    print("Database 'task_database' created successfully!")

def create_recipe():
    print("Creating recipe...")

def search_recipe():
    print("Searching recipe...")

def update_recipe():
    print("Updating recipe...")

def delete_recipe():
    print("Deleting recipe...")

def main_menu():
    while True:
        print("\n=== Recipe Management System ===")
        print("1. Create recipe")
        print("2. Search recipe")
        print("3. Update recipe")
        print("4. Delete recipe")
        print("5. Exit (or type 'quit')")
        
        choice = input("Enter your choice: ").strip().lower()
        
        if choice in ["1", "create", "add"]:
            create_recipe()
        elif choice in ["2", "search", "find"]:
            search_recipe()
        elif choice in ["3", "update", "edit"]:
            update_recipe()
        elif choice in ["4", "delete", "remove"]:
            delete_recipe()
        elif choice in ["5", "quit", "exit", "q"]:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # create_database()
    main_menu()