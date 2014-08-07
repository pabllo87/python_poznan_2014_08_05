class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _update_bree(item):
        if item.quality <50:
            if item.sell_in > 0:
                item.quality += 1
            else:
                item.quality += 2
        item.quality = item.quality if item.quality <= 50 else 50
        item.sell_in -= 1

    def _update_tickets(item):
        if item.sell_in <= 0:
            item.quality = 0

        if 0 <= item.quality < 50 and item.sell_in > 0:
            if item.sell_in > 10:
                item.quality += 1
            elif 5 < item.sell_in <=10:
                item.quality += 2
            elif item.sell_in <= 5:
                item.quality += 3
        item.quality = item.quality if item.quality <= 50 else 50
        item.sell_in -= 1

    def _update_sulfuras(item):
        pass

    def _update_item(item):
        if item.quality > 0:
            if item.sell_in > 0:
                item.quality -= 1
            else:
                item.quality -= 2
        item.quality = item.quality if item.quality >=0 else 0
        item.sell_in -= 1

    def _update_conjured(item):
        if item.quality > 0:
            if item.sell_in > 0:
                item.quality -= 2
            else:
                item.quality -= 4
        item.quality = item.quality if item.quality >=0 else 0
        item.sell_in -= 1

    item_updates = {
        'Aged Brie' : _update_bree,
        'Backstage passes to a TAFKAL80ETC concert' : _update_tickets,
        'Sulfuras, Hand of Ragnaros' : _update_sulfuras,
        'Conjured' : _update_conjured
    }

    def update_quality(self):
        for item in self.items:
            try:
                item.update(item)
            except AttributeError:
                item.update = GildedRose.item_updates.get(item.name,
                                                          GildedRose._update_item)
                item.update(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
