class ToyRobot:
    def __init__(self, table_size):
        self.x = None
        self.y = None
        self.facing = None
        self.table_size = table_size

    def place(self, x, y, facing):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
            facing (_type_): _description_
        """
        if self.is_in_bounds(x, y) and self.is_valid_direction(facing):
            self.x = x
            self.y = y
            self.facing = facing

    def move(self):
        """_summary_
        """
        if self.x is None or self.y is None or self.facing is None:
            print("Cannot move")
            return

        if self.facing == "NORTH" and self.y < self.table_size - 1:
            self.y += 1
        elif self.facing == "SOUTH" and self.y > 0:
            self.y -= 1
        elif self.facing == "EAST" and self.x < self.table_size - 1:
            self.x += 1
        elif self.facing == "WEST" and self.x > 0:
            self.x -= 1

    def left(self):
        """_summary_
        """
        if self.facing is None:
            return
        if self.facing == "NORTH":
            self.facing = "WEST"
        elif self.facing == "WEST":
            self.facing = "SOUTH"
        elif self.facing == "SOUTH":
            self.facing = "EAST"
        elif self.facing == "EAST":
            self.facing = "NORTH"

    def right(self):
        """_summary_
        """
        if self.facing is None:
            return
        if self.facing == "NORTH":
            self.facing = "EAST"
        elif self.facing == "EAST":
            self.facing = "SOUTH"
        elif self.facing == "SOUTH":
            self.facing = "WEST"
        elif self.facing == "WEST":
            self.facing = "NORTH"

    def report(self):
        """_summary_

        Returns:
            _type_: _description_
        """        
        if self.x is None or self.y is None or self.facing is None:
            return "Robot is not placed on the table."
        return f"{self.x},{self.y},{self.facing}"

    def is_in_bounds(self, x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        return 0 <= x < self.table_size and 0 <= y < self.table_size

    def is_valid_direction(self, facing):
        """_summary_

        Args:
            facing (_type_): _description_

        Returns:
            _type_: _description_
        """
        return facing in ["NORTH", "SOUTH", "EAST", "WEST"]
