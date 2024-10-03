def fibonacci(n):
    # print(f"n={n}")
    if n <= 1:
        print(f'Non recursive case f{n} = {n}')
        return n
    else:
        print(f'Recursive case f{n} = f{n-1} + f{n-2}')
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
