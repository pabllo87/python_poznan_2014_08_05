class Vector:
    def __init__(self, pos):
        self.__pos = pos

    @property
    def pos(self):
        return self.__pos

    def __add__(self, other):
        return Vector((other.pos[0]+self.pos[0],
                      other.pos[1]+self.pos[1]))

    @pos.setter
    def pos(self, new_pos):
        self.__pos = new_pos

    def __eq__(self, other):
        return self.__pos == other

class N_Direction:
    def move_forward(self):
        return Vector((0, 1))

    def move_backward(self):
        return Vector((0, -1))

    def turn_right(self):
        return E_Direction()

    def turn_left(self):
        return W_Direction()

    def __repr__(self):
        return 'N'

    def __eq__(self, other):
        return 'N' == other

class E_Direction:
    def move_forward(self):
        return Vector((1, 0))

    def move_backward(self):
        return Vector((-1, 0))

    def turn_right(self):
        return S_Direction()

    def turn_left(self):
        return N_Direction()

    def __repr__(self):
        return 'E'

    def __eq__(self, other):
        return 'E' == other

class S_Direction:
    def move_forward(self):
        return Vector((0, -1))

    def move_backward(self):
        return Vector((0, 1))

    def turn_right(self):
        return W_Direction()

    def turn_left(self):
        return E_Direction()

    def __repr__(self):
        return 'S'

    def __eq__(self, other):
        return 'S' == other

class W_Direction:
    def move_forward(self):
        return Vector((-1, 0))

    def move_backward(self):
        return Vector((1, 0))

    def turn_right(self):
        return N_Direction()

    def turn_left(self):
        return S_Direction()

    def __repr__(self):
        return 'W'

    def __eq__(self, other):
        return 'W' == other

class Rover:
    def __init__(self):
        self.position = Vector((0, 0))
        self.direction = N_Direction()

    def move(self, list_of_commands):
        for command in list_of_commands:
            self.single_move(command)

    def single_move(self, command):
        if command == 'f':
            self.position += self.direction.move_forward()
        elif command == 'r':
            self.direction = self.direction.turn_right()
        elif command == 'l':
            self.direction = self.direction.turn_left()
        elif command == 'r':
            self.position += self.direction.turn_backward()
        else:
            raise TypeError("unknown sequence")
