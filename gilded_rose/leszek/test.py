class Item:
    def __init__(self):
        self.attr = 123

    def update(self):
        self.update_function(self)


def update_item_by_2(self):
    self.attr += 2


def update_item_by_3(self):
    self.attr += 2
