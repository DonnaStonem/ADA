def facto(x):
    if x == 0 or x == 1:
        print(f"base case, fact {x} is ", x)
        return 1
    else:
        print(f"recursive case, n={x}, return {x} * fact{x-1}")
        return x * facto(x - 1)

print(facto(5))
