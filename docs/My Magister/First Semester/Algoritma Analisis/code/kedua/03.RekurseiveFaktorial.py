def recursive(x):

    if x in range (0,1):
        return 1
    
    return recursive(x-1) * x


print(recursive(3))
