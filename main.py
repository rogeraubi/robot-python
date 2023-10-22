"""
This module provides utilities for handling system-related tasks.
It uses the 'sys' module for various system-level operations.
"""

import sys
from toy_robot import ToyRobot

def main():
    """_summary_
    """
    table_size = 5
    robot = ToyRobot(table_size)

    while True:
        choice = input(
            "Choose an option:\n1. Enter commands directly\n2. Process commands from a file\n3. Exit\n")

        if choice == '1':
            # Enter commands directly
            while True:
                command = input(
                    "Enter a command (PLACE X,Y,F, MOVE, LEFT, RIGHT, REPORT, or QUIT): ")
                handle_commands(robot, command)

        elif choice == '2':
            # Process commands from a file
            file_path = input(
                "Enter the path to the command file (default: data/command.txt): ")
            if not file_path:
                file_path = 'data/command.txt'
            process_file_commands(robot, file_path)

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


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
        or command == "QUIT"
        or command.startswith("PLACE ")
    )


def place_command(robot, command_args):
    """_summary_

    Args:
        robot (_type_): _description_
        command_args (_type_): _description_
    """
    x, y, facing = command_args.split(',')
    robot.place(int(x), int(y), facing)


def handle_commands(robot, command):
    """_summary_

    Args:
        robot (_type_): _description_
        command (_type_): _description_
    """
    if command.strip().upper() == 'QUIT' or (not is_valid_command(command)):
        print("Goodbye! Thank you for using the Toy Robot Simulator or wrong commands")
        sys.exit()
    else:
        parts = command.strip().upper().split(' ')
        command_name = parts[0]
        if command_name == 'PLACE':
            place_command(robot, parts[1])
        elif command_name == 'MOVE':
            robot.move()
        elif command_name == 'LEFT':
            robot.left()
        elif command_name == 'RIGHT':
            robot.right()
        elif command_name == 'REPORT':
            print(robot.report())
        else:
            print('Invalid command')


def process_file_commands(robot, file_path):
    """_summary_

    Args:
        robot (_type_): _description_
        file_path (_type_): _description_
    """
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            commands = file.read().splitlines()
            print(f"Content of file '{file_path}':")
            print(" -> ".join(commands))
            print("\n**result**\n")
            for command in commands:
                handle_commands(robot, command)
    except FileNotFoundError:
        print(
            f"File '{file_path}' does not exist. Please provide a valid file path.")


if __name__ == "__main__":
    main()
