from datetime import datetime
import os
import time
import string
from random import randint

def log(func):
    def wrapper(*args, **kwargs):
        funcname = func.__name__
        name = funcname.split('_')
        string = ""
        for i in name:
            string += i.capitalize() + ' '
        phrase = '(' + os.environ.get('USER') + ')Running: ' + string + ' '
        phrase = phrase.ljust(35, ' ')
        phrase += "[ exec-time = {} ]"
        starttime = datetime.now()
        response = func(*args, **kwargs)
        # print("--- {} seconds ---".format(datetime.now() - starttime))
        print(phrase.format(datetime.now() - starttime))
        return response
    return wrapper

# TO-DO : write in file `machine.log` instead of print()

class CoffeeMachine():

    water_level = 100

    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
    
## Terminal
# boiling...
# Coffee is ready!
# boiling...
# Coffee is ready!
# boiling...
# Coffee is ready!
# boiling...
# Coffee is ready!
# Please add water!
# Please add water!
# Blub blub blub...

## cat machine.log
# (cmaxime)Running: Start Machine 	[ exec-time = 0.001 ms ]
# (cmaxime)Running: Boil Water 	    [ exec-time = 0.005 ms ]
# (cmaxime)Running: Make Coffee 	    [ exec-time = 2.499 s  ]
# (cmaxime)Running: Start Machine 	[ exec-time = 0.002 ms ]
# (cmaxime)Running: Boil Water 	    [ exec-time = 0.005 ms ]
# (cmaxime)Running: Make Coffee 	    [ exec-time = 2.618 s  ]
# (cmaxime)Running: Start Machine 	[ exec-time = 0.003 ms ]
# (cmaxime)Running: Boil Water 	    [ exec-time = 0.004 ms ]
# (cmaxime)Running: Make Coffee 	    [ exec-time = 2.676 s  ]
# (cmaxime)Running: Start Machine 	[ exec-time = 0.003 ms ]
# (cmaxime)Running: Boil Water 	    [ exec-time = 0.004 ms ]
# (cmaxime)Running: Make Coffee 	    [ exec-time = 2.648 s  ]
# (cmaxime)Running: Start Machine 	[ exec-time = 0.011 ms ]
# (cmaxime)Running: Make Coffee 	    [ exec-time = 0.029 ms ]
# (cmaxime)Running: Start Machine 	[ exec-time = 0.009 ms ]
# (cmaxime)Running: Make Coffee 	    [ exec-time = 0.024 ms ]
# (cmaxime)Running: Add Water 	    [ exec-time = 5.026 s  ]