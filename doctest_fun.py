def add(a, b):
    """Adds two objects using + operator

    >>> add(2, 3)
    5
    >>> add('a', 'b')
    'ab'
    >>> l1 = [1,2,3]
    >>> l2 = [4,5,6]
    >>> add(l1, l2)
    [1, 2, 3, 4, 5, 6]
    >>> add(1, '1')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a+b

def fibonacci(n):
    """Returns n-th fibonacci number

    >>> [fibonacci(x) for x in range(10)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
