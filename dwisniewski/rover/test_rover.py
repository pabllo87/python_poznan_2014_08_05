import pytest
from rover import Rover


@pytest.fixture
def r():
    return Rover()


def test_mars_rover_start_at_0_0(r):
    assert r.position == [0, 0]


def test_mars_rover_start_at_north(r):
    assert r.direction == ('y', 1)


@pytest.mark.parametrize('command, expected', [
    ('r', ('x', 1)),
    (4*'r', ('y', 1)),
])
def test_mars_rover_direction(r, command, expected):
    r.move(command)
    assert r.direction == expected


def test_mars_rover_other_commnad(r):
    with pytest.raises(TypeError):
        r.move('z')


@pytest.mark.parametrize('command, expected', [
    ('f', [0, 1]),
    ('ff', [0, 2]),
    ('rff', [2, 0]),
    ('rfflf', [2, 1]),
    ('ffb', [0, 1]),
    (10*'f', [0, 10]),
    (11*'f', [0, 0]),
    ('r'+11*'f', [0, 0]),
])
def test_mars_rover_position(r, command, expected):
    r.move(command)
    assert r.position == expected


def test_size_of_planet(r):
    assert r.grid_size == [10, 10]
