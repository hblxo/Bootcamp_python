import sys

def op(nb1, nb2):
    print("Sum:        ", nb1 + nb2)
    print("Difference: ", nb1 - nb2)
    print("Product:    ", nb1 * nb2)
    try:
        print("Quotient:   ", nb1 / nb2)
    except ZeroDivisionError:
        print("Quotient:    ERROR (div by zero)")
    try:
        print("Remainder:    ", nb1 % nb2)
    except ZeroDivisionError:
        print("Remainder:   ERROR (modulo by zero)")
    
try:
    len_arg = len(sys.argv) - 1
    if (len < 2):
        raise TypeError
    if (len_arg > 2):
        raise RuntimeError("Too Many Arguments")
    op(int(sys.argv[1]), int(sys.argv[2]))
except TypeError: 
    print("Usage: python operations.py <number1> <number2>")
    print("\tExample:\n\t\tpython operations.py 10 3")
except ValueError:
    print("InputError: only numbers")
except RuntimeError as e:
    print(e)
    sys.exit(1)
