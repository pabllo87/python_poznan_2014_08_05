class MoveError(BaseException):
    pass


class World(object):
    
    def __init__(self, size=100):
        self.size = size
        self.directions = ['n', 'e', 's', 'w']
        self.obstacles = {}
    
    def get(self, loc):
        return self.obstacles.get('{}_{}'.format(loc[0], loc[1]))
    
    def put(self, loc, obj):
        self.obstacles['{}_{}'.format(loc[0], loc[1])] = obj;


class Rover(object):

    def __init__(self, world, x=0, y=0, direction='n'):
        self.world = world
        self.location = [x, y]
        self.dirAngle = self.world.directions.index(direction)

    def command(self, cmds):
        for cmd in cmds:
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

    @property
    def direction(self):
        return self.world.directions[self.dirAngle]

    def move(self, distance):
        axis = (self.dirAngle+1) % 2
        headingNE = 1 if self.dirAngle < 2 else -1
        new_loc = list(self.location)
        new_loc[axis] = (new_loc[axis] + headingNE * distance) % self.world.size
        if self.world.get(new_loc):
            raise MoveError()
        self.location = new_loc
        
    def turn(self, angle):
        self.dirAngle = (self.dirAngle + angle) % len(self.world.directions)