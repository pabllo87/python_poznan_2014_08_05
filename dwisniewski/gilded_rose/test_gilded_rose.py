import pytest
from gilded_rose_original import (
    GildedRose,
    Item
)


@pytest.fixture
def rose():
    return GildedRose([])


@pytest.fixture
def rabbit():
    return Item('rabbit', 10, 10)


@pytest.fixture
def misc_items():
    return [Item('rabbit', sell_in=10, quality=10),
            Item('cheap beer', sell_in=4, quality=15)]


@pytest.fixture
def ab():
    return Item('Aged Brie', sell_in=10, quality=49)


@pytest.fixture
def sulfuras():
    return Item('Sulfuras, Hand of Ragnaros', sell_in=5, quality=7)


def test_add_items_to_gd(rose, rabbit):
    rose.items.append(rabbit)
    assert len(rose.items) == 1


def test_aging_generic_item(rose, rabbit):
    rose.items.append(rabbit)
    rose.update_quality()
    assert rose.items[0].quality == 9
    assert rose.items[0].sell_in == 9


def test_adding_misc_items_and_aging_them(rose, misc_items):
    rose.items.extend(misc_items)
    rose.update_quality()
    assert rose.items[0].quality == 9
    assert rose.items[0].sell_in == 9
    assert rose.items[1].quality == 14
    assert rose.items[1].sell_in == 3


def test_quality_degrades_twice_when_sell_passed(rose):
    rose.items.append(Item('rabbit', sell_in=-1, quality=10))
    rose.update_quality()
    assert rose.items[0].quality == 8
    assert rose.items[0].sell_in == -2


def test_quality_never_negative(rose):
    rose.items.append(Item('rabbit', sell_in=-1, quality=1))
    rose.update_quality()
    assert rose.items[0].quality == 0
    assert rose.items[0].sell_in == -2


def test_aged_brie_incrase_quality(rose, ab):
    rose.items.append(ab)
    rose.update_quality()
    assert rose.items[0].quality == 50
    assert rose.items[0].sell_in == 9


def test_aged_brie_incrase_quality_no_more_50(rose, ab):
    rose.items.append(ab)
    rose.update_quality()
    assert rose.items[0].quality == 50
    assert rose.items[0].sell_in == 9
    rose.update_quality()
    assert rose.items[0].quality == 50
    assert rose.items[0].sell_in == 8


def test_slufuras_never_sold_or_decrease_quality(rose, sulfuras):
    rose.items.append(sulfuras)
    rose.update_quality()
    assert rose.items[0].quality == 7
    assert rose.items[0].sell_in == 5


def test_backstage_passes_increase_quality(rose):
    rose.items.append(Item('Backstage passes to a TAFKAL80ETC concert', sell_in=12, quality=1))
    rose.update_quality()
    assert rose.items[0].quality == 2
    assert rose.items[0].sell_in == 11


def test_backstage_passes_increase_quality_2_when_sell_in_lte_10(rose):
    rose.items.append(Item('Backstage passes to a TAFKAL80ETC concert', sell_in=10, quality=1))
    rose.update_quality()
    assert rose.items[0].quality == 3
    assert rose.items[0].sell_in == 9


def test_backstage_passes_increase_quality_3_when_sell_in_lte_5(rose):
    rose.items.append(Item('Backstage passes to a TAFKAL80ETC concert', sell_in=5, quality=1))
    rose.update_quality()
    assert rose.items[0].quality == 4
    assert rose.items[0].sell_in == 4


def test_backstage_passes_drop_quality_when_sell_in_lt_0(rose):
    rose.items.append(Item('Backstage passes to a TAFKAL80ETC concert', sell_in=0, quality=10))
    rose.update_quality()
    assert rose.items[0].quality == 0
    assert rose.items[0].sell_in == -1


def test_aging_conjured_item(rose):
    rose.items.append(Item('Conjured', sell_in=5, quality=10))
    rose.update_quality()
    assert rose.items[0].quality == 8
    assert rose.items[0].sell_in == 4


def test_aging_conjured_item_sell_out(rose):
    rose.items.append(Item('Conjured', sell_in=0, quality=10))
    rose.update_quality()
    assert rose.items[0].quality == 6
    assert rose.items[0].sell_in == -1
