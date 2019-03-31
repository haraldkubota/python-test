def factorial(n: int) -> int:
    """
    Return factorial of a number (>=0)
    >>> factorial(3)
    6
    >>> factorial(4)
    24
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
