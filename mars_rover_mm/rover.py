class PlanetMap:

    def __init__(self, size):
        self.size = size

    def map_size(self):
        return self.size

    def is_obstacle(self, param):
        return False


class Rover:

    def __init__(self):
        self.pos = (0, 0)
        self.current_direction = 'N'
        self.directions = ['N', 'E', 'S', 'W']
        self.movements = {
            'N': (0, 1),
            'E': (1, 0),
            'S': (0, -1),
            'W': (-1, 0),
        }
        self.map_size = 10

    def position(self):
        return self.pos

    def direction(self):
        return self.current_direction

    def _turn(self, clockwise):
        turn_factor = 1
        if not clockwise:
            turn_factor = -1
        direction_id = self.directions.index(self.current_direction)
        self.current_direction = self.directions[(direction_id + turn_factor) % 4]

    def _move(self, forward):
        move_factor = 1
        if not forward:
            move_factor = -1
        vector = self.movements[self.current_direction]
        self.pos = (
            (self.pos[0] + move_factor * vector[0]) % self.map_size,
            (self.pos[1] + move_factor * vector[1]) % self.map_size
        )

    def move(self, commands):
        for command in commands:
            if command == 'f':
                self._move(forward=True)
            if command == 'b':
                self._move(forward=False)
            elif command == 'r':
                self._turn(clockwise=True)
            elif command == 'l':
                self._turn(clockwise=False)