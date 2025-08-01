from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker 

Base = declarative_base()

engine = create_engine("mysql://cf-python:paroladordineperpythonmysql@localhost/my_database")

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

session.add(tea)
session.add(coffee)
session.add(cake)
session.commit()

print(tea.id)