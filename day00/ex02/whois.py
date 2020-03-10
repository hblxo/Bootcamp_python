import sys

if (len(sys.argv) - 1 != 1):
    print("ERROR")
    exit()

try:
    arg = int(sys.argv[1])
except ValueError:
    print("ERROR")
    exit()
    
# if (type(arg) != int):
#     exit()

if (arg % 2):
    print("I'm Odd.")
elif (arg == 0):
    print("I'm Zero.")
else:
    print("I'm Even.")
