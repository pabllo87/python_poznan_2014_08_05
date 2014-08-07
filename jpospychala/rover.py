class MoveError(BaseException):
    pass

class World(object):
    def __init__(self, size=100):
        self.size = size
        self.obstacles = {}
    
    def get(self, loc):
        return self.obstacles.get('{}_{}'.format(loc[0], loc[1]))
    
    def put(self, loc, obj):
        self.obstacles['{}_{}'.format(loc[0], loc[1])] = obj;

class Rover(object):
    
    def __init__(self, world, x=0, y=0, direction='n'):
        self._directions = ['n', 'e', 's', 'w']
        self.world = world
        self.location = [x, y]
        self.direction = direction

    def commands(self, cmdarray):
        for cmd in cmdarray:
            self.command(cmd)

    def command(self, cmd):
        if cmd is 'f':
            self.move(1)
        elif cmd is 'r':
            self.turn(1)
        elif cmd is 'l':
            self.turn(-1)
        elif cmd is 'b':
            self.move(-1)
        else:
            raise TypeError()

    def move(self, distance):
        axis = (self._directions.index(self.direction)+1) % 2
        new_loc = list(self.location)
        new_loc[axis] = (new_loc[axis] + distance) % self.world.size
        if self.world.get(new_loc):
            raise MoveError()
        self.location = new_loc
        
    def turn(self, angle):
        idx = self._directions.index(self.direction)
        idx = (idx + angle) % len(self._directions)
        self.direction = self._directions[idx]