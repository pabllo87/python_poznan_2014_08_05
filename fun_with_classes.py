class A:
    def __init__(self):
        self.attr = 123

    def method(self):
        self.attr = 234

class B(A):
    def __init__(self):
        super().__init__()

    def method(self):
        #super().method()
        A.method(self)
