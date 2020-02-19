#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Janell Huyck, Koren Niles, Chris Wilson"


def add(x, y):
    """Add two integers. Handles negative values."""
    sum = x + y
    return sum


print(add(2, 4))


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    result = 0

    if x < 0:
        pos_x = 0 - x
    else:
        pos_x = x
    if y < 0:
        pos_y = 0 - y
    else:
        pos_y = y

    for num in range(pos_x):
        result = add(result, pos_y)
    if x < 0 and y < 0:
        return result
    if x < 0 or y < 0:
        return 0 - result

    return result


print(multiply(6, -8))


def power(x, n):
    """Raise x to power n, where n >= 0"""
    result = 1
    for num in range(n):
        result = multiply(x, result)
    return result


print(power(2, 8))


def factorial(x):
    """Compute factorial of x, where x > 0"""
    result = 1
    for num in range(x, 1, -1):
        result = multiply(num, result)
    return result


print(factorial(4))


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n < 2:
        return 0
    if n <= 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(8))


if __name__ == '__main__':
    # your code to call functions above
    pass
