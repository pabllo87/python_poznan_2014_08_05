class RUL:
    def __init__(self):
        self.rul = []

    def empty(self):
        return not self.rul

    def add(self, item):
        if item in self.rul:
            self.rul.remove(item)
        self.rul.append(item)

    def size(self):
        return len(self.rul)

    def first(self):
        return self.rul[-1]

    def __getitem__(self, index):
        return self.rul[-1-index]
    
