import unittest
from rover import Rover, World, MoveError

class RoverTest(unittest.TestCase):

    def setUp(self):
        self.w = World()
        self.r = Rover(world=self.w)

    def test_mars_rover_starts_at_0_0(self):
        self.assertEquals([0, 0], self.r.location)
    
    def test_mars_rover_starts_facing_north(self):
        self.assertEquals('n', self.r.direction)
    
    def test_mars_rover_accepts_commands(self):
        try:
            self.r.command('rf')
        except Exception:
            self.fail("Expected to issue commands")

    def test_mars_rover_accepts_only_chars_array(self):
        with self.assertRaises(TypeError):
            self.r.command([0,1,2,3])
    
    def test_that_moves_forward(self):
        self.r.command('f')
        self.assertEquals([0, 1], self.r.location)
    
    def test_that_moves_fwd_fwd(self):
        self.r.command('ff')
        self.assertEquals([0, 2], self.r.location)
        
    def test_that_cmd_right_turns_east(self):
        self.r.command('r')
        self.assertEquals('e', self.r.direction)
    
    def test_that_cmd_rr_turns_south(self):
        self.r.command('rr')
        self.assertEquals('s', self.r.direction)
    
    def test_that_cmd_rrr_turns_west(self):
        self.r.command('rrr')
        self.assertEquals('w', self.r.direction)
    
    def test_that_cmd_5x_r_turns_east(self):
        self.r.command('rrrrr')
        self.assertEquals('e', self.r.direction)

    def test_that_cmd_l_turns_west(self):
        self.r.command('l')
        self.assertEquals('w', self.r.direction)
    
    def test_that_cmd_5x_l_turns_west(self):
        self.r.command('lllll')
        self.assertEquals('w', self.r.direction)
    
    def test_that_cmd_b_moves_backward(self):
        self.r.command('fb')
        self.assertEquals([0, 0], self.r.location)
    
    def test_that_moves_fwd_horizontally(self):
        self.r.command('rf')
        self.assertEquals([1, 0], self.r.location)

    def test_that_ffrff_moves_to_2_2(self):
        self.r.command('ffrff')
        self.assertEquals([2, 2], self.r.location)

    def test_that_ffrff_moves_to_2_2(self):
        self.r.command('frrf')
        self.assertEquals([0, 0], self.r.location)

    def test_that_edges_are_wrapped(self):
        self.r.command('f'*self.w.size)
        self.assertEquals([0, 0], self.r.location)
    
    def test_that_cant_move_over_obstacle(self):
        self.w.put([1, 1], "tree")
        with self.assertRaises(MoveError):
            self.r.command("frf")
        self.assertEquals([0, 1], self.r.location)
    
class WorldTest(unittest.TestCase):

    def setUp(self):
        self.w = World()

    def test_world_size_is_100(self):
        self.assertEquals(100, self.w.size)
    
    def test_can_find_objects_by_location(self):
        self.assertEquals(None, self.w.get([0, 0]))
    
    def test_can_put_objects(self):
        self.w.put([0, 0], 'obstacle')
        self.assertEquals('obstacle', self.w.get([0, 0]))