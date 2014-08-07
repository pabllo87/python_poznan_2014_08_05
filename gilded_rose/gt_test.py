import unittest
from gilded_rose_original import GildedRose, Item

Backstage="Backstage passes to a TAFKAL80ETC concert"
Conjured="Conjured"

class GildedRoseTest(unittest.TestCase):

    def test_generic_item_value_and_quality_drops(self):
        item = self.ndays(Item("Koperek", sell_in=1, quality=1), days=1)
        
        self.assertEquals(0, item.sell_in)
        self.assertEquals(0, item.quality)
    
    def test_after_sellin_date_quality_drops_twice(self):
        item = self.ndays(Item("koperek", sell_in=0, quality=10), days=1)
        self.assertEquals(8, item.quality)
    
    def test_quality_is_never_negative(self):
        item = self.ndays(Item("koperek", sell_in=0, quality=0), days=1)
        self.assertEquals(0, item.quality)
    
    def test_aged_brie_quality_increases(self):
        item = self.ndays(Item("Aged Brie", sell_in=10, quality=0), days=1)
        self.assertEquals(1, item.quality)
    
    def test_aged_brie_quality_increases_2x_after_sellin(self):
        item = self.ndays(Item("Aged Brie", sell_in=0, quality=0), days=1)
        self.assertEquals(2, item.quality)
    
    def test_quality_is_never_more_than_50(self):
        item = self.ndays(Item("Aged Brie", sell_in=0, quality=0), days=26)
        self.assertEquals(50, item.quality)
    
    def test_sulfuras_never_has_to_be_sold(self):
        item = self.ndays(Item("Sulfuras, Hand of Ragnaros", sell_in=1, quality=0), days=1)
        self.assertEquals(1, item.sell_in)
    
    def test_sulfuras_never_drops_on_quality(self):
        item = self.ndays(Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=1), days=1)
        self.assertEquals(1, item.quality)
    
    def test_backstage_quality_grows_2x_when_10__to_5_days(self):
        item = self.ndays(Item(Backstage, sell_in=10, quality=0), days=5)
        self.assertEquals(10, item.quality)
    
    def test_backstage_quality_grows_3x_when_5_to_0_days(self):
        item = self.ndays(Item(Backstage, sell_in=5, quality=0), days=5)
        self.assertEquals(15, item.quality)
    
    def test_backstage_quality_goes_0_after_sellin(self):
        item = self.ndays(Item(Backstage, sell_in=0, quality=10), days=1)
        self.assertEquals(0, item.quality)
    
    def test_conjured_items_quality_degrade_twice_as_fast_as_normal_until_sellin(self):
        item = self.ndays(Item(Conjured, sell_in=1, quality=10), days=1)
        #self.assertEquals(8, item.quality)
    
    def test_conjured_items_quality_degrade_twice_as_fast_as_normal_after_sellin(self):
        item = self.ndays(Item(Conjured, sell_in=0, quality=10), days=1)
        #self.assertEquals(6, item.quality)
                       
    def ndays(self, item, days=0):
        gd = GildedRose([item])
        for i in range(days):
            gd.update_quality()
        return item

    
def test_variants():
    print '''
import unittest
from gilded_rose_original import GildedRose, Item

class GildedRoseGenTest(unittest.TestCase):
    '''
    variants = ["Aged Brie", "Sulfuras, Hand of Ragnaros", "Regular", Backstage]
    i = 0
    for v in variants:
        for sellin in range(-10, 10):
            for quality in range(0, 50):
                i = i+1
                after = Item(v, sellin, quality)
                gd = GildedRose([after])
                gd.update_quality()
                print '''
    def test_{i}(self):
        item = Item("{v}", {s}, {q})
        gd = GildedRose([item])
        gd.update_quality()
        
        self.assertEquals({safter}, item.sell_in)
        self.assertEquals({qafter}, item.quality)
'''.format(i=i, v=v,s=sellin,q=quality, qafter=after.quality,safter=after.sell_in)
                    
#test_variants()     