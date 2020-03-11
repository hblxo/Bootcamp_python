import sys

# count the arguments
arguments = len(sys.argv) - 1

# output argument-wise
position = 1
str = ""
while (arguments >= position):
    str = str + sys.argv[position]
    if (arguments > 1 and position < arguments):
        str = str + " "
    position = position + 1
newstring = ""
for a in str: 
# Checking for lowercase letter and converting to uppercase. 
    if (a.isupper()) == True: 
        newstring+=(a.lower())
    elif (a.islower()) == True:
        newstring+=(a.upper())
    else:
        newstring+=(a)

print(newstring[::-1])