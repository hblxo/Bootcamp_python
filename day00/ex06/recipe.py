import sys

cookbook = {
    'sandwich':
    {
        'ingredients': ('ham', 'bread', 'cheese', 'tomatoes'),
        'meal':'lunch',
        'prep_time':10
    },
    'cake':
    {
        'ingredients': ('flour', 'sugar', 'eggs'),
        'meal':'dessert',
        'prep_time':60
    },
    'salad':
    {
        'ingredients': ('avocado', 'arugula', 'tomatoes', 'spinach'),
        'meal':'lunch',
        'prep_time':15
    }
}

#1 
# for key, value in cookbook.items():
#     print(key)
    # for k, v in value.items():
    #     print(v)

#2
def print_recipe(name):
    print("\n")
    for key, value in cookbook.items():
        if (name == key):
            print("Recipe for", name, ":")
            print("Ingredients list:", value.get('ingredients'))
            print("To be eaten for", value.get('meal'))
            print("Takes", value.get('prep_time'), "minutes of cooking.\n")
                
# print_recipe("salad")

#3
def del_recipe(name):
    cookbook.pop(name)
    print("Recipe ", name, "deleted\n")

# print("---------      before pop      ------------")
# print_recipe('salad')    
# del_recipe('salad')
# print("---------       after pop      ------------")
# print_recipe('salad')

#4
def add_recipe(name, ingredients, meal, time):
    recipe = {
        'ingredients':ingredients,
        'meal':meal,
        'prep_time':time
        }
    cookbook[name] = recipe
      
# add_recipe('test',  ('avocado', 'arugula', 'tomatoes'), 'lunch', 154)
# print_recipe('test')

#5
def print_names():
    print("\n")
    for key, value in cookbook.items():
        print(">", key)
    print("\n")

#print_names()

#6
def print_choices():
    print("\nPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n\n")
    
choice = 0
while(choice != 5):
    try:
        print_choices()
        choice = int(input())
        assert choice <= 5 and choice > 0
        if (choice == 1):
            try:
                print("Name :")
                name = str(input())
                print("Ingredients :")
                ingr = str(input())
                # ingr.split(',',' ')
                print("Meal :")
                meal = str(input())
                print("Time :")
                time = int(input())
                add_recipe(name, ingr, meal, time)
            except:
                print("Wrong type")
        elif (choice == 2):
            print("Please enter the recipe's name")
            name = str(input())
            del_recipe(name)
        elif (choice == 3):
            print("Please enter the recipe's name")
            name = str(input())
            print_recipe(name)
        elif (choice == 4):
            print_names()
        elif (choice == 5):
            print("Cookbook closed")    
            pass
        else:
            pass
    except :
        print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    
