import pytest
from gilded_rose import GildedRose, Item

@pytest.fixture
def rose():
	return GildedRose([])

@pytest.fixture
def rabbit():
	return Item("rabbit", 10, 10)

@pytest.fixture
def misc_items():
	return [Item("rabbit", sell_in=10, quality=10),
			Item("cheap beer", sell_in=5, quality=15)]

@pytest.fixture
def misc_poor_items():
	return [Item("rabbit", sell_in=1, quality=4),
			Item("cheap beer", sell_in=3, quality=4)]

@pytest.fixture
def bree_item():
	return [Item("Aged Brie", sell_in=1, quality=40)]

@pytest.fixture
def pass_item():
	return [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=30)]

@pytest.fixture
def sulfuras_item():
	return [Item("Sulfuras, Hand of Ragnaros", sell_in=15, quality=30)]

def test_inserting_generic_item(rose, rabbit):
	rose.items.append(rabbit)

def test_aging_generic_item(rose, rabbit):
	rose.items.append(rabbit)
	rose.update_quality()
	assert rose.items[0].sell_in == 9
	assert rose.items[0].quality == 9

def test_adding_misc_items_and_aging_them(rose, misc_items):
	rose.items.extend(misc_items)
	rose.update_quality()
	assert rose.items[0].sell_in == 9
	assert rose.items[0].quality == 9
	assert rose.items[1].sell_in == 4
	assert rose.items[1].quality == 14

def test_adding_misc_items_and_aging_them_past_sell_date(rose, misc_poor_items):
	rose.items.extend(misc_poor_items)
	rose.update_quality()
	rose.update_quality()
	assert rose.items[0].sell_in == -1
	assert rose.items[0].quality == 1
	assert rose.items[1].sell_in == 1
	assert rose.items[1].quality == 2

def test_quality_is_not_negative(rose, misc_poor_items):
	rose.items.extend(misc_poor_items)
	for _ in range(4):  #four days
		rose.update_quality()
	assert rose.items[0].sell_in == -3
	assert rose.items[0].quality == 0

def test_bree_increases_quality(rose, bree_item):
	rose.items.extend(bree_item)
	rose.update_quality()
	assert rose.items[0].quality == 41

def test_bree_quality_doesnt_excess_50(rose, bree_item):
	rose.items.extend(bree_item)
	for _ in range(20):
		rose.update_quality()
	assert rose.items[0].quality == 50

def test_sulfuras_doesnt_decrease_in_quality(rose, sulfuras_item):
	rose.items.extend(sulfuras_item)
	for _ in range(20):
		rose.update_quality()
	assert rose.items[0].quality == 30

def test_backstage_items_increase_quality_if_more_than_10_days(rose, pass_item):
	rose.items.extend(pass_item)
	rose.update_quality()
	assert rose.items[0].quality == 31

def test_backstage_items_increase_quality_by_2_if_less_than_10_days(rose, pass_item):
	rose.items.extend(pass_item)
	rose.items[0].sell_in = 9
	rose.update_quality()
	assert rose.items[0].quality == 32

def test_backstage_items_increase_quality_by_3_if_less_than_5_days(rose, pass_item):
	rose.items.extend(pass_item)
	rose.items[0].sell_in = 4
	rose.update_quality()
	assert rose.items[0].quality == 33

@pytest.fixture
def conjured_item():
	return [Item("Conjured", sell_in=10, quality=10)]

def test_conjured_item_ages_faster(rose, conjured_item):
	rose.items.extend(conjured_item)
	rose.update_quality()
	assert rose.items[0].quality == 8

def test_conjured_item_even_faster_after_date(rose, conjured_item):
	rose.items.extend(conjured_item)
	rose.items[0].sell_in = 0
	rose.update_quality()
	assert rose.items[0].quality == 6