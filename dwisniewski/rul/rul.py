from collections import deque


class RUL(object):

    def __init__(self, limit=None):
        self.__limit = limit
        self.__list = deque(maxlen=self.__limit)

    def empty(self):
        return self.size() == 0

    def add(self, item):
        if item in self.__list:
            self.__list.remove(item)
        if item:
            self.__list.appendleft(item)

    def first(self):
        return self.__list[0]

    def size(self):
        return len(self.__list)

    def __getitem__(self, index):
        return self.__list[index]

    def __iter__(self):
        for x in self.__list:
            yield x

    def get_limit(self):
        return self.__limit
