from unittest import TestCase
from mars_rover_mm.rover import Rover, PlanetMap


class TestMap(TestCase):
    def test_should_return_map_size(self):
        map = PlanetMap(101)
        self.assertEqual(101, map.map_size())

    def test_should_not_contain_any_obstacles_at_start(self):
        map = PlanetMap(1)
        self.assertFalse(map.is_obstacle((0, 0)))


class TestRover(TestCase):

    def setUp(self):
        self.rover = Rover()

    def test_rover_starts_at_0_0(self):
        self.assertEqual((0, 0), self.rover.position())

    def test_rover_starts_facing_north(self):
        self.assertEqual('N', self.rover.direction())

    def test_should_r_turn_rover_right(self):
        self.rover.move('r')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('E', self.rover.direction())

        self.rover.move('r')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('S', self.rover.direction())

        self.rover.move('r')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('W', self.rover.direction())

        self.rover.move('r')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('N', self.rover.direction())

    def test_should_l_turn_rover_left(self):
        self.rover.move('l')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('W', self.rover.direction())

        self.rover.move('l')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('S', self.rover.direction())

        self.rover.move('l')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('E', self.rover.direction())

        self.rover.move('l')
        self.assertEqual((0, 0), self.rover.position())
        self.assertEqual('N', self.rover.direction())

    def test_should_accept_multiple_commands(self):
        self.rover.move('fr')
        self.assertEqual((0, 1), self.rover.position())
        self.assertEqual('E', self.rover.direction())

    def test_should_rover_move_forward_north_when_facing_north(self):
        self.rover.move('f')
        self.assertEqual((0, 1), self.rover.position())
        self.assertEqual('N', self.rover.direction())

    def test_should_rover_move_forward_east_when_facing_east(self):
        self.rover.move('rf')
        self.assertEqual((1, 0), self.rover.position())
        self.assertEqual('E', self.rover.direction())

    def test_should_rover_move_forward_south_when_facing_south(self):
        self.rover.move('rrf')
        self.assertEqual((0, 9), self.rover.position())
        self.assertEqual('S', self.rover.direction())

    def test_should_rover_move_forward_west_when_facing_west(self):
        self.rover.move('lf')
        self.assertEqual((9, 0), self.rover.position())
        self.assertEqual('W', self.rover.direction())

    def test_should_rover_move_backward_south_when_facing_north(self):
        self.rover.move('b')
        self.assertEqual((0, 9), self.rover.position())
        self.assertEqual('N', self.rover.direction())

    def test_should_rover_move_backward_west_when_facing_east(self):
        self.rover.move('rb')
        self.assertEqual((9, 0), self.rover.position())
        self.assertEqual('E', self.rover.direction())

    def test_should_rover_move_backward_north_when_facing_south(self):
        self.rover.move('rrb')
        self.assertEqual((0, 1), self.rover.position())
        self.assertEqual('S', self.rover.direction())

    def test_should_rover_move_backward_east_when_facing_west(self):
        self.rover.move('lb')
        self.assertEqual((1, 0), self.rover.position())
        self.assertEqual('W', self.rover.direction())

    def test_should_up_and_down_edges_connect(self):
        self.rover.move('b')
        self.assertEqual((0, 9), self.rover.position())

        self.rover.move('f')
        self.assertEqual((0, 0), self.rover.position())

    def test_should_left_and_right_edges_connect(self):
        self.rover.move('lf')
        self.assertEqual((9, 0), self.rover.position())

        self.rover.move('b')
        self.assertEqual((0, 0), self.rover.position())
