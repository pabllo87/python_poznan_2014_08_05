class AClass:
    def __init__(self):
        self.attr = 123

    def __getattr__(self, name):
        print(name)
        return AClass()
