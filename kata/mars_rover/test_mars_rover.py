import unittest
from mars_rover import Rover, Vector

class MarsRoverTests(unittest.TestCase):
    def setUp(self):
        self.rover = Rover()

    def test_mars_rover_starts_at_0_0(self):
        self.assertEqual((0,0), self.rover.position)

    def test_mars_rover_starts_facing_north(self):
        self.assertEqual('N', self.rover.direction)

    def test_mars_rover_accepts_f_command(self):
        self.rover.move('f')
        self.assertEqual((0, 1), self.rover.position)

    def test_mars_rover_accepts_r_command(self):
        self.rover.move('r')
        self.assertEqual('E', self.rover.direction)

    def test_mars_rover_rejects_other_commands(self):
        with self.assertRaises(TypeError):
            self.rover.move('z')

    def test_mars_rover_accepts_rf_command(self):
        self.rover.move('rf')

    def test_mars_rover_moves_to_1_1_on_frf(self):
        self.rover.move('frf')
        self.assertEqual((1,1), self.rover.position)

    def test_mars_rover_rolls(self):
        self.rover.move(4*'r')
        self.assertEqual('N', self.rover.direction)
        self.assertEqual((0,0), self.rover.position)

class VecTest(unittest.TestCase):
    def test_vector_creating_and_getting(self):
        v = Vector((1,1))
        self.assertEqual((1,1), v.pos)

    def test_vector_setter(self):
        v = Vector((1,1))
        v.pos = 2, 2
        self.assertEqual((2,2), v.pos)

    def test_vector_additions(self):
        v1 = Vector((1,1))
        v2 = Vector((2,2))
        v3 = v1 + v2
        self.assertEqual((3,3), v3.pos)

    def test_vector_to_tuple_comp(self):
        self.assertEqual((1,1), Vector((1,1)))