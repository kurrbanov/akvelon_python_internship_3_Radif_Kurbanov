def fibonacci(n):
    fib0 = 0
    fib1 = 1

    if n < 0:
        return None
    if n == 0:
        return fib0
    if n == 1:
        return fib1

    for i in range(2, n + 1):
        fib3 = fib1 + fib0
        fib0 = fib1
        fib1 = fib3

    return fib1


print(fibonacci(8))
