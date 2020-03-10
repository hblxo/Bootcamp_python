
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
for key, value in cookbook.items():
    print(key)
    for k, v in value.items():
        print(v)

#2
def print_recipe(name):
    for key, value in cookbook.items():
        if (name == key):
            for k, v in value.items():
                print(v)