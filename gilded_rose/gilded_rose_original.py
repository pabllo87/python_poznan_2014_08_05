# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    item.quality = item.quality - item.quality
            elif item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.quality < 50:
                    if item.sell_in < 0:
                        item.quality = item.quality + 1
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Conjured":
                item.sell_in -= 1
                if item.quality > 0:
                    item.quality = item.quality - 2
                if item.quality > 0:
                    if item.sell_in < 0:
                        item.quality = item.quality - 2
            else: # regular
                item.sell_in = item.sell_in - 1
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.quality > 0:
                    if item.sell_in < 0:
                        item.quality = item.quality - 1

    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
