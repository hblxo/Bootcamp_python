def ft_filter(function_to_apply, list_of_inputs):
    try:
        assert callable(function_to_apply)
        assert list_of_inputs != None
        iter(list_of_inputs)
        res = []
        for i in list_of_inputs:
            if function_to_apply(i):
                res.append(i)
        return res
    except:
        print("Error")


print("----Test Map with a tuple of numbers----")
def isOdd(n):
    if n % 2:
        return True
    else:
        return False

numbers = (1, 2, 3, 4)
result = ft_filter(isOdd, numbers)
print(result)
