# -*- coding: utf-8 -*-


class GildedRose(object):

    def _update_normal(self, i):
        i.quality -= 1 if i.sell_in > 0 else 2
        i.quality = 0 if i.quality < 0 else i.quality
        i.sell_in -= 1

    def _update_ab(self, i):
        i.sell_in -= 1
        i.quality += 1 if i.quality < 50 else 0
        i.quality += 1 if i.sell_in < 0 and i.quality < 50 else 0

    def _update_backstage(self, i):
        if i.sell_in > 0:
            i.quality += 1 if i.quality < 50 else 0
            i.quality += 1 if i.sell_in < 11 and i.quality < 50 else 0
            i.quality += 1 if i.sell_in < 6 and i.quality < 50 else 0
        else:
            i.quality = 0
        i.sell_in -= 1

    def _update_sulfuras(self, i):
        pass

    def _update_conjured(self, i):
        self._update_normal(i)
        self._update_normal(i)
        i.sell_in += 1

    def __init__(self, items):
        self.items = items
        self.update_func = {
            'Aged Brie': self._update_ab,
            'Backstage passes to a TAFKAL80ETC concert': self._update_backstage,
            'Sulfuras, Hand of Ragnaros': self._update_sulfuras,
            'Conjured': self._update_conjured,
        }

    def update_quality(self):
        for item in self.items:
            self.update_func.get(item.name, self._update_normal)(item)


class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
