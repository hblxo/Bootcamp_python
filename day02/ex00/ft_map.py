def ft_map(function_to_apply, list_of_inputs):
    try:
        assert callable(function_to_apply)
        assert list_of_inputs != None
        # input_type = type(list_of_inputs)
        iter(list_of_inputs)
        res = []
        for i in list_of_inputs:
            res.append(function_to_apply(i))
        return res
    except:
        print("Error")


print("----Test Map with a tuple of numbers----")
def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = ft_map(calculateSquare, numbers)
print(result)

print("----Test Map with a list of strings----")
def ft_upper(string):
    newstr = ""
    for c in string:
        if c.islower():
            newstr += c.upper()
        else:
            newstr += c
    return newstr

strings = "test", "str", "rokb,vfl"
result = ft_map(ft_upper, strings)
print(result)
