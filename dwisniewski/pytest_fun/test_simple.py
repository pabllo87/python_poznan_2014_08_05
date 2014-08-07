def fibonacci(n):
    """Returns n-th fibonacci number
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return b

import pytest


@pytest.mark.parametrize("inp, out", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5)
])
def test_fibonacci(inp, out):
    assert fibonacci(inp) == out


def test_dictionaries():
    assert {'a': 0, 'd': 1, 'c': 2} == {'a': 0, 'd': 1, 'c': 2}


def test_looong_list():
    l1 = 100*[1] + [2] + 100*[1]
    l2 = 100*[1] + [2] + 100*[1]
    assert l1 == l2
