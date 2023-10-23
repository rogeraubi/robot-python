import click
from enum import Enum


class Direction(Enum):
    """_summary_

    Args:
        Enum (_type_): _description_
    """
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class ToyRobot:
    """_summary_
    """

    def __init__(self, table_size):
        self._x = None
        self._y = None
        self._facing = None
        self._table_size = table_size

    @property
    def is_placed(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return all((self._x is not None, self._y is not None, self._facing is not None))

    def _is_valid_position(self, x, y):
        return 0 <= x < self._table_size and 0 <= y < self._table_size

    def _rotate_left(self):
        if self.is_placed:
            if self._facing.value - 1 == 0:
                self._facing = Direction(4)
            else:
             self._facing = Direction((self._facing.value - 1) % 4)
    def _rotate_right(self):
        if self.is_placed:
            self._facing = Direction((self._facing.value + 1) % 4)

    def _move(self):
        if not self.is_placed:
            return

        new_x, new_y = self._x, self._y

        if self._facing == Direction.NORTH:
            new_y += 1
        elif self._facing == Direction.EAST:
            new_x += 1
        elif self._facing == Direction.SOUTH:
            new_y -= 1
        elif self._facing == Direction.WEST:
            new_x -= 1

        if self._is_valid_position(new_x, new_y):
            self._x, self._y = new_x, new_y

    def place(self, x, y, facing):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
            facing (_type_): _description_
        """
        if Direction.__members__.get(facing):
            if self._is_valid_position(x, y):
                self._x, self._y, self._facing = x, y, Direction[facing]

    def report(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.is_placed:
            return f"{self._x},{self._y},{self._facing.name}"
        return "Robot is not placed on the table."


def is_valid_command(command):
    """_summary_

    Args:
        command (_type_): _description_

    Returns:
        _type_: _description_
    """
    command = command.strip().upper()
    return (
        command == "MOVE"
        or command == "LEFT"
        or command == "RIGHT"
        or command == "REPORT"
        or command.startswith("PLACE ")
    )


def handle_commands(robot, command):
    """_summary_

    Args:
        robot (_type_): _description_
        command (_type_): _description_
    """
    parts = command.strip().upper().split(' ')
    command_name = parts[0]

    if command_name == 'PLACE':
        place_args = parts[1].split(',')
        if len(place_args) == 3:
            x, y, facing = place_args
            robot.place(int(x), int(y), facing)
    elif command_name == 'MOVE':
        robot._move()
    elif command_name == 'LEFT':
        robot._rotate_left()
    elif command_name == 'RIGHT':
        robot._rotate_right()
    elif command_name == 'REPORT':
        click.echo(robot.report())
    else:
        click.echo('Invalid command')


@click.command()
@click.option("--table-size", type=int, default=5, help="Size of the table (default: 5)")
@click.option("--file", type=click.File(), help="Process commands from a file")
def main(table_size=5, file=None):
    """_summary_

    Args:
        table_size (int, optional): _description_. Defaults to 5.
        file (_type_, optional): _description_. Defaults to None.
    """
    click.echo(f"Welcome to the Toy Robot Simulator! Table size: {table_size}")
    robot = ToyRobot(table_size)
    if file:
        # Process commands from a file
        click.echo("Processing commands from a file...")
        for line in file:
            handle_commands(robot, line.strip())
    else:
        # Enter commands directly
        click.echo("Enter commands directly. Type 'QUIT' to exit.")
        while True:
            command = click.prompt("> ", type=str)
            if command.strip().upper() == 'QUIT':
                break
            handle_commands(robot, command)

    click.echo("Goodbye!")


if __name__ == "__main__":
    main()
