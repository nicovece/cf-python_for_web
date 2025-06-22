# CareerFoundry - Python for Web Developers

## Exercise 1.2 Data types in python

### Create a data structure for your Recipe app

### Rationale for Data Structure Selection

#### `recipe`

For the recipe object, a `dictionary` was the most obvious choice because the structure consisted of three key-value pairs, such as `"recipe_name": "Pasta"`. Dictionaries also allow values of any data type, which enabled me to store the recipe name as a string, the cooking time as an integer, and the ingredients as a list.

#### `all_recipes`

I used a `list` for `all_recipes` to store the individual recipe dictionaries. This provided a sequential structure while still allowing me to store complex data for each recipe and easily access or manipulate their contents.
