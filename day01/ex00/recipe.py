
class Recipe:										#	Defining 'Recipe' class
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):	#	Method called when creating an object
		self.name = name							#	Attribute of class Recipe. This one stocks name for ex
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type
		try:
			if type(name) == str and name != "" is False:
				raise RuntimeError("Name should be a string and should not be empty")
			if type(cooking_lvl) == int and cooking_lvl > 0 and cooking_lvl < 6 is False:
				raise RuntimeError("Cooking level must be between 1 and 5")
			if type(cooking_time) == int and cooking_time > 0 is False:
				raise RuntimeError("cooking-time should not be negative")
			if type(ingredients) == list and len(ingredients) != 0 is False:
				raise RuntimeError("Ingredients can only be a list and must not be empty")
			if type(description) != str:
				raise RuntimeError("Description should only be a string")
			if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
				raise RuntimeError("Wrong type of recipe")
		except RuntimeError as e:
			print(e)
			exit()
	
	#	Defining a str method to print properly all information about a recipe
	def __str__(self):
		"""Return the string to print with the recipe info"""
		text = "The name of this recipe is {}, on a difficulty cooking scale up to five, it is a {}.\nIt takes {} minutes to cook.\nIt has the following ingredients : {}.\nHere is a quick description : {}.\nThis recipe is a {}.\nBon appetit !".format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
		return text
		