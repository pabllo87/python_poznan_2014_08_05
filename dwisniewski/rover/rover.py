class Rover(object):

    def __init__(self, x=0, y=0, direction=('y', 1), grid_x=10, grid_y=10):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__direction_list = [
            ('y', 1),
            ('x', 1),
            ('y', -1),
            ('x', -1)
        ]
        self.__grid_x = grid_x
        self.__grid_y = grid_y

    def __set_attr(self, name, value):
        pos = getattr(self, name)
        grid = getattr(self, 'grid_'+name)
        pos += value
        if pos > grid:
            pos = 0
        elif pos < 0:
            pos = grid
        return pos

    @property
    def grid_x(self):
        return self.__grid_x

    @property
    def grid_y(self):
        return self.__grid_y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, go):
        self.__x = self.__set_attr('x', go)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, go):
        self.__y = self.__set_attr('y', go)

    @property
    def position(self):
        return [self.__x, self.__y]

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, cmd):
        move = 1 if cmd == 'r' else -1

        index = self.__direction_list.index(self.direction)
        if index + 1 >= len(self.__direction_list):
            index = 0
        else:
            index = index + move
        self.__direction = self.__direction_list[index]

    @property
    def grid_size(self):
        return [self.__grid_x, self.__grid_y]

    def move(self, command):
        for x in command:
            self._command(x)

    def _command(self, command):
        if command in 'fb':
            go = self.direction[1] if command == 'f' else -self.direction[1]
            if self.direction[0] == 'y':
                self.y = go
            if self.direction[0] == 'x':
                self.x = go
        elif command in 'rl':
            self.direction = command
        else:
            raise TypeError("unknown ssequence")
