class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        rules = [
            {'name': 'Backstage passes to a TAFKAL80ETC concert', 'quality': 1},
            {'name': 'Backstage passes to a TAFKAL80ETC concert', 'sell_in_lt': 11, 'quality': 1},
            {'name': 'Backstage passes to a TAFKAL80ETC concert', 'sell_in_lt': 6, 'quality': 1},
            {'name': 'Backstage passes to a TAFKAL80ETC concert', 'sell_in': -1},
            {'name': 'Backstage passes to a TAFKAL80ETC concert', 'sell_in_lt': 0, 'quality': -100},
            {'name': 'Aged Brie', 'sell_in': -1, 'quality': 1},
            {'name': 'Aged Brie', 'sell_in_lt': 0, 'quality': 1},
            {'name': 'Conjured', 'sell_in': -1},
            {'name': 'Conjured', 'quality_gt': 0, 'quality': -2},
            {'name': 'Conjured', 'quality_gt': 0, 'sell_in_lt': 0, 'quality': -2},
            {'name_not_in': ['Backstage passes to a TAFKAL80ETC concert', 'Aged Brie', 'Conjured', 'Sulfuras, Hand of Ragnaros'], 'sell_in': -1},
            {'name_not_in': ['Backstage passes to a TAFKAL80ETC concert', 'Aged Brie', 'Conjured', 'Sulfuras, Hand of Ragnaros'], 'quality_gt': 0, 'quality': -1},
            {'name_not_in': ['Backstage passes to a TAFKAL80ETC concert', 'Aged Brie', 'Conjured', 'Sulfuras, Hand of Ragnaros'], 'quality_gt': 0, 'sell_in_lt': 0, 'quality': -1},
        ]
        for item in self.items:
            for r in rules:
                if item.name == r.get('name', item.name) and not item.name in r.get('name_not_in', [])  and r.get('sell_in_gt', item.sell_in-1) < item.sell_in < r.get('sell_in_lt', item.sell_in+1) and r.get('quality_gt', item.quality-1) < item.quality < r.get('quality_lt', item.quality+1):
                    item.quality, item.sell_in = max(min(item.quality + r.get('quality', 0), 50), 0), item.sell_in + r.get('sell_in', 0)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
