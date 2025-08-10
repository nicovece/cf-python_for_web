from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker 
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

engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")

Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    __tablename__ = "practice_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

Base.metadata.create_all(engine)

tea = Recipe(
    name="Tea",
    cooking_time=5,
    ingredients="Tea leaves, Water, Sugar"
)

coffee = Recipe(
    name="Coffee",
    cooking_time=5,
    ingredients="Coffee Powder, Sugar, Water"
)

cake = Recipe(
    name="Cake",
    cooking_time=50,
    ingredients="Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk"
)

banana_smoothie = Recipe(
    name="Banana Smoothie",
    cooking_time=5,
    ingredients="Bananas, Milk, Peanut Butter, Sugar, Ice Cubes"
)



session.add(tea)
session.add(coffee)
session.add(cake)
session.add(banana_smoothie)
session.commit()

print(tea.id)

sugar_recipes_contains = session.execute(select(Recipe).where(Recipe.ingredients.contains('Sugar'))).scalars().all()

print(f"Found {len(sugar_recipes_contains)} recipes with contains")

# Print the actual recipes
for recipe in sugar_recipes_contains:
    print(f"Recipe: {recipe.name}")

sugar_recipes_like = session.execute(select(Recipe).where(Recipe.ingredients.like('%Sugar%'))).scalars().all()

print(f"Found {len(sugar_recipes_like)} recipes with like")

for recipe in sugar_recipes_like:
    print(f"Recipe: {recipe.name}")

condition_list = [
    Recipe.ingredients.like("%Milk%"),
    Recipe.ingredients.like("%Baking Powder%")
]

recipes_with_both = session.execute(select(Recipe).where(*condition_list)).scalars().all()
print(f"Found {len(recipes_with_both)} recipes with both Milk AND Baking Powder:")
for recipe in recipes_with_both:
    print(f"Recipe: {recipe.name} - Ingredients: {recipe.ingredients}")