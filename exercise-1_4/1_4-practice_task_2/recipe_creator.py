import pickle

recipe = {
    'name': 'Tea',
    'ingredients': ['tea', 'water', 'sugar'],
    'cooking_time': '5 minutes',
    'difficulty': 'easy'
}

recipe_file = open('exercise-1_4/1_4-practice_task_2/recipe_binary.bin', 'wb')
pickle.dump(recipe, recipe_file)
recipe_file.close()

with open('exercise-1_4/1_4-practice_task_2/recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe details - ")
print("Name:  " + recipe['name'])
print("Ingredients: " + str(recipe['ingredients']))
print("Cooking time: " + recipe['cooking_time'])
print("Difficulty: " + recipe['difficulty'])