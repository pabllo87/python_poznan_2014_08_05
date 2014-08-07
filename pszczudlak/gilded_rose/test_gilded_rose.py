import pytest
from gilded_rose import GildedRose, Item

def jump_days(rose, days):
	for _ in range(days):
		rose.update_quality()

def _test_with_items(items, days, sell_in, quality):
	rose = GildedRose(items)
	jump_days(rose, days)
	assert items[0].sell_in == sell_in
	assert items[0].quality == quality

@pytest.mark.parametrize('days, sell_in, quality', [
	(1, 2, 9), (3, 0, 7), (4, -1, 5), (5, -2, 3),
	(6, -3, 1), (7, -4, 0), (8, -5, 0)
])
def test_basic_item(days, sell_in, quality):
	_test_with_items([Item('Belt', 3, 10)], days, sell_in, quality)

@pytest.mark.parametrize('days, sell_in, quality', [
	(1, 4, 41), (2, 3, 42), (5, 0, 45), (6, -1, 47)
])
def test_aged_items(days, sell_in, quality):
	_test_with_items([Item('Aged Brie', 5, 40)], days, sell_in, quality)

def test_quality_never_more_than_50():
	_test_with_items([Item('Aged Brie', 5, 45)], 20, -15, 50)

@pytest.mark.parametrize('days, sell_in, quality', [
	(1, 5, 40), (2, 5, 40), (100, 5, 40)
])
def test_legendary_items(days, sell_in, quality):
	_test_with_items([Item('Sulfuras, Hand of Ragnaros', 5, 40)], days, sell_in, quality)

@pytest.mark.parametrize('days, sell_in, quality', [
	(1, 11, 2), (2, 10, 3), (3, 9, 5), (4, 8, 7), (5, 7, 9),
	(7, 5, 13), (8, 4, 16), (9, 3, 19), (10, 2, 22), (11, 1, 25),
	(12, 0, 28), (13, -1, 0), (15, -3, 0)
])
def test_backstage_passes(days, sell_in, quality):
	_test_with_items([Item('Backstage passes to a TAFKAL80ETC concert', 12, 1)], days, sell_in, quality)

@pytest.mark.parametrize('days, sell_in, quality', [
	(1, 1, 8), (2, 0, 6), (3, -1, 2)
])
def test_conjured_items(days, sell_in, quality):
	_test_with_items([Item('Conjured', 2, 10)], days, sell_in, quality)
