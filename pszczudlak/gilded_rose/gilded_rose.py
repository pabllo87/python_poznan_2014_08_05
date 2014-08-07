class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self.item_funcs = {
            'Aged Brie': lambda i: self._update_item(i, 1),
            'Backstage passes to a TAFKAL80ETC concert': self.update_ticket_item,
            'Conjured': lambda i: self._update_item(i, -2),
            'Sulfuras, Hand of Ragnaros': lambda _: None
        }

    def _update_item(self, item, val=-1):
        item.sell_in -= 1
        if item.sell_in < 0:
            val *= 2
        item.quality = max(min(50, item.quality + val), 0)

    def update_ticket_item(self, item):
        self._update_item(item, abs((item.sell_in - 1) / 5 - 3))
        if item.sell_in < 0:
            item.quality = 0

    def update_quality(self):
        for item in self.items:
            self.item_funcs.get(item.name, self._update_item)(item)

    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
