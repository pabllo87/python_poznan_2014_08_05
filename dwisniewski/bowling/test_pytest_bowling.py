from bowling import PlayerScore
import pytest


@pytest.fixture
def g():
    return PlayerScore()


def nroll(g, n, pins):
    for i in range(n):
        g.roll(pins)


def test_gutter_game(g):
    nroll(g, 20, 0)
    assert g.score() == 0


@pytest.mark.parametrize("nrolls, pins, expected", [
    (20, 1, 20),
    (20, 2, 40),
    (21, 5, 150),
    (12, 10, 300),
])
def test_fixed_scores(g, nrolls, pins, expected):
    nroll(g, nrolls, pins)
    assert g.score() == expected
