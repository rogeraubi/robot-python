import unittest
from unittest.mock import patch
from io import StringIO
from .uiRobot import ToyRobot, handle_commands, is_valid_command


class TestToyRobot(unittest.TestCase):

    def setUp(self):
        self.robot = ToyRobot(5)

    def test_place(self):
        self.robot.place(1, 2, "NORTH")
        self.assertEqual(self.robot.report(), "1,2,NORTH")

    def test_invalid_place(self):
        self.robot.place(6, 0, "NORTH")
        self.assertEqual(self.robot.report(),
                         "Robot is not placed on the table.")

    def test_move(self):
        self.robot.place(0, 0, "NORTH")
        self.robot._move()
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_rotate_left(self):
        self.robot.place(1, 1, "NORTH")
        self.robot._rotate_left()
        self.assertEqual(self.robot.report(), "1,1,WEST")

    def test_rotate_right(self):
        self.robot.place(0, 0, "NORTH")
        self.robot._rotate_right()
        self.assertEqual(self.robot.report(), "0,0,EAST")

    def test_report_unplaced(self):
        self.assertEqual(self.robot.report(),
                         "Robot is not placed on the table.")

    def test_valid_command(self):
        self.assertTrue(is_valid_command("MOVE"))
        self.assertTrue(is_valid_command("LEFT"))
        self.assertTrue(is_valid_command("RIGHT"))
        self.assertTrue(is_valid_command("REPORT"))
        self.assertTrue(is_valid_command("PLACE 1,2,NORTH"))

    def test_invalid_command(self):
        self.assertFalse(is_valid_command("INVALID"))
        self.assertTrue(is_valid_command("PLACE 1,2,NORTH"))
        self.assertFalse(is_valid_command(""))

    def test_handle_commands(self):
        self.robot.place(0, 0, "NORTH")  # Place the robot first
        command = "MOVE\nREPORT"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            commands = command.split("\n")
            for command in commands:
                handle_commands(self.robot, command)
        self.assertEqual(self.robot.report(), "0,1,NORTH")
        self.assertEqual(mock_stdout.getvalue(), "0,1,NORTH\n")


if __name__ == "__main__":
    unittest.main()
