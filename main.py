from numbers import factorial, fibonacci


def factorial(n):   # return factorial value of n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 4)


print(factorial(5))
print(fibonacci(5))
