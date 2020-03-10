t = (19,42,21)

count = 0
to_print = "The 3 numbers are: "
for i in t:
    to_print += str(i)
    count += 1
    if (count < 3):
        to_print += ", " 
        
print(to_print)

# print("The 3 numbers are: %d, %d, %d" % (t[0], t[1], t[2]))