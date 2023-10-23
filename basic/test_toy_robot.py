import unittest
from .toy_robot import ToyRobot

class TestToyRobot(unittest.TestCase):
    def test_place_method(self):
        robot = ToyRobot(5)
        robot.place(1, 2, "NORTH")
        self.assertEqual(robot.report(), "1,2,NORTH")

    def test_move_method(self):
        robot = ToyRobot(5)
        robot.place(0, 0, "NORTH")
        robot.move()
        self.assertEqual(robot.report(), "0,1,NORTH")

    def test_left_method(self):
        robot = ToyRobot(5)
        robot.place(1, 2, "NORTH")
        robot.left()
        self.assertEqual(robot.report(), "1,2,WEST")

    def test_right_method(self):
        robot = ToyRobot(5)
        robot.place(1, 2, "NORTH")
        robot.right()
        self.assertEqual(robot.report(), "1,2,EAST")

    def test_report_method_when_not_placed(self):
        robot = ToyRobot(5)
        self.assertEqual(robot.report(), "Robot is not placed on the table.")

    def test_is_in_bounds_method(self):
        robot = ToyRobot(5)
        self.assertTrue(robot.is_in_bounds(3, 4))
        self.assertFalse(robot.is_in_bounds(6, 7))

    def test_is_valid_direction_method(self):
        robot = ToyRobot(5)
        self.assertTrue(robot.is_valid_direction("NORTH"))
        self.assertTrue(robot.is_valid_direction("SOUTH"))
        self.assertTrue(robot.is_valid_direction("EAST"))
        self.assertTrue(robot.is_valid_direction("WEST"))
        self.assertFalse(robot.is_valid_direction("UP"))

if __name__ == "__main__":
    unittest.main()
